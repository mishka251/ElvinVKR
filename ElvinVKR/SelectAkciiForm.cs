using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Newtonsoft.Json.Linq;
using System.IO;

namespace ElvinVKR
{

    public struct stockInfo
    {
        public string name;
        public string code;
        public int id;

        public stockInfo(int id, string code, string name)
        {
            this.id = id;
            this.name = name;
            this.code = code;
        }


    }



    public partial class SelectAkciiForm : Form
    {
        public SelectAkciiForm()
        {
            InitializeComponent();
        }
        List<stockInfo> allStocks;
        JArray akcii;
        private void btnLoadFile_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.ShowDialog();
            allStocks = new List<stockInfo>();

            string file = ofd.FileName;

            StreamReader sr = new StreamReader(file);
            string akc = sr.ReadToEnd();
            sr.Close();

            akcii = JArray.Parse(akc);

            for (int i = 0; i < akcii.Count; i++)
            {
                string name = (string)akcii[i]["name"];
                dataGridView1.Rows.Add(name, false);
                allStocks.Add(new stockInfo((int)akcii[i]["id"], (string)akcii[i]["code"], (string)akcii[i]["name"]));
            }
        }

        private void btnCalc_Click(object sender, EventArgs e)
        {
            List<stockInfo> stocks = new List<stockInfo>();
            for (int i = 0; i < dataGridView1.RowCount; i++)
            {
                if ((bool)dataGridView1.Rows[i].Cells[1].Value)
                {
                    stocks.Add(allStocks[i]);
                }
            }

            Form1 f1 = new Form1(stocks);
            f1.Show();

        }
    }
}
