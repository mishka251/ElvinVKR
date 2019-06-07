using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using System.Diagnostics;
using System.IO;
using Newtonsoft.Json.Linq;

namespace ElvinVKR
{
    public partial class Form1 : Form
    {
        List<stockInfo> stocksList;
        public Form1(List<stockInfo> stocks = null)
        {
            InitializeComponent();

            string exeDir = Directory.GetCurrentDirectory();
            DirectoryInfo info = new DirectoryInfo(exeDir);
            DirPath = info.Parent.Parent.FullName;

            if (stocks != null)
            {
                stocksList = stocks;
            }

        }

        JArray allPortfels;
        JObject bestPorts;

        string DirPath;

        private static void run_cmd(string cmd, string args)
        {
            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = cmd;//cmd is full path to python.exe
            start.Arguments = args;//args is path to .py file and any cmd line args
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                    Console.Write(result);
                }
                process.Close();
            }
        }


        void LoadAllPorts()
        {
            string file = DirPath + "/portfels.json";
            StreamReader sr = new StreamReader(file);
            string json = sr.ReadToEnd();
            sr.Close();

            allPortfels = JArray.Parse(json);
        }

        void LoadBestPorts()
        {
            string file = DirPath + "/output.json";
            StreamReader sr = new StreamReader(file);
            string json = sr.ReadToEnd();
            sr.Close();

            bestPorts = JObject.Parse(json);
        }

        void ShowAllPorts()
        {
            dataGridView1.Columns.Clear();

            dataGridView1.Columns.Add("percsCol", "Проенты");
            //dataGridView1.Columns.Add("namesCol", "Названия");
            dataGridView1.Columns.Add("m1Col", "м1");
            dataGridView1.Columns.Add("m2Col", "м2");
            dataGridView1.Columns.Add("dohodCol", "Доходность");

            for (int i = 0; i < allPortfels.Count; i++)
            {
                JObject obj = (JObject)allPortfels[i];
                object[] arr = { obj["percs"],/*, obj["names"],*/ obj["m1"], obj["m2"], obj["dohod"] };
                dataGridView1.Rows.Add(arr);
                dataGridView1.Rows[i].HeaderCell.Value = (i + 1) + "";

                for (int j = 0; j < keys.Length; j++)
                {
                    string key = keys[j];
                    JObject obj2 = (JObject)bestPorts[key][1];

                    bool eq = true;
                    for (int k = 0; k < ((JArray)obj["percs"]).Count; k++)
                    {
                        eq &= ((double)((JArray)obj["percs"])[k]) == ((double)((JArray)obj2["percs"])[k]);
                        //eq &= ((string)((JArray)obj["names"])[k]) == ((string)((JArray)obj2["names"])[k]);
                    }

                    for (int k = 0; k < ((JArray)obj["percs"]).Count; k++)


                        if (eq)// if (obj["percs"].Equals(obj2["percs"]) && obj["names"].Equals(obj2["names"]))
                        {
                            if (key == "minM1" || key == "maxM1")
                                dataGridView1.Rows[i].Cells[1].Style.BackColor = colorForbestVal[key];

                            else
                                dataGridView1.Rows[i].Cells[2].Style.BackColor = colorForbestVal[key];
                        }
                }
            }
            dataGridView1.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells;
            dataGridView1.RowHeadersWidthSizeMode = DataGridViewRowHeadersWidthSizeMode.AutoSizeToAllHeaders;
        }

        string[] keys = { "minM1", "minM2", "maxM1", "maxM2" };
        Dictionary<string, Color> colorForbestVal = new Dictionary<string, Color>()
                {
            {"minM1", Color.Yellow },
            {"minM2", Color.Red },
            {"maxM1", Color.Blue },
            {"maxM2", Color.Green }

        };

        void ShowBestPorts()
        {
            dataGridView2.Columns.Clear();

            dataGridView2.Columns.Add("percsCol", "Проенты");
            // dataGridView2.Columns.Add("namesCol", "Названия");
            dataGridView2.Columns.Add("m1Col", "м1");
            dataGridView2.Columns.Add("m2Col", "м2");
            dataGridView2.Columns.Add("dohodCol", "Доходность");



            string bestKey = keys[0];
            JObject bestObj = ((JObject)bestPorts[keys[0]][1]);
            double bestDohod = (double)bestObj["dohod"];

            for (int i = 0; i < keys.Length; i++)
            {
                string key = keys[i];
                JObject obj = (JObject)bestPorts[key][1];
                object[] arr = { obj["percs"], /*obj["names"], */obj["m1"], obj["m2"], obj["dohod"] };
                dataGridView2.Rows.Add(arr);
                dataGridView2.Rows[i].HeaderCell.Value = key;


                double dohod = (double)obj["dohod"];
                if (dohod > bestDohod)
                {
                    bestDohod = dohod;
                    bestObj = obj;
                    bestKey = key;
                }

            }
            dataGridView2.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells;
            dataGridView2.AutoSizeRowsMode = DataGridViewAutoSizeRowsMode.AllCells;
            dataGridView2.RowHeadersWidthSizeMode = DataGridViewRowHeadersWidthSizeMode.AutoSizeToAllHeaders;

            richTextBox1.Text = $"Лучший доход {bestDohod}\n" +
                $"Достигается при показателе {bestKey}\n" +
                $"Портфель {bestObj["percs"]}";// {bestObj["names"]}";
            setStat(bestKey);
        }
        const string filename = "stat.txt";
        private void button1_Click(object sender, EventArgs e)
        {
            //OpenFileDialog ofd = new OpenFileDialog();
            //ofd.ShowDialog();
           // string fname = ofd.FileName;//.Replace(@"\\", @"\");

            // string leng = "5";
            string alph = "0.05";
            string k = "0.4";
            string pythonPath = "python";//@"C:\python_django\python.exe";

            string cmd = DirPath + @"\pyCode\main.py";

            string args = $" \"{cmd}\" {alph} {k} \"{ DirPath + @"\portfels.json"}\" \"{DirPath + @"\output.json"}\"";

            for (int i = 0; i < stocksList.Count; i++)
            {
                args += $" {stocksList[i].id} {stocksList[i].code}";
            }


            run_cmd(pythonPath, args);

            LoadAllPorts();
            LoadBestPorts();

            ShowAllPorts();
            ShowBestPorts();
        }

        void setStat(string best)
        {
            int m1Max = 0;
            int m1Min = 0;
            int m2Min = 0;
            int m2Max = 0;
            try
            {
                StreamReader sr = new StreamReader(filename);
                m1Max = int.Parse(sr.ReadLine());
                m1Min = int.Parse(sr.ReadLine());
                m2Min = int.Parse(sr.ReadLine());
                m2Max = int.Parse(sr.ReadLine());
                sr.Close();
            }
            catch (Exception)
            {

            }


            switch (best)
            {
                case "minM1": m1Min++; break;
                case "minM2": m2Min++; break;
                case "maxM1": m1Max++; break;
                case "maxM2": m2Max++; break;

                default:
                    break;
            }
            StreamWriter sw = new StreamWriter(filename);
            sw.WriteLine($"{m1Max}");
            sw.WriteLine($"{m1Min}");
            sw.WriteLine($"{m2Min}");
            sw.WriteLine($"{m2Max}");
            sw.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Stiatistic stat = new Stiatistic();
            stat.Show();
        }
    }
}
