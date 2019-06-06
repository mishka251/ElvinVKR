using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
namespace ElvinVKR
{
    public partial class Stiatistic : Form
    {
        const string filename = "stat.txt";

      
        public Stiatistic()
        {
            InitializeComponent();
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


            StreamWriter sw = new StreamWriter(filename);
            sw.WriteLine($"{m1Max}");
            sw.WriteLine($"{m1Min}");
            sw.WriteLine($"{m2Min}");
            sw.WriteLine($"{m2Max}");
            sw.Close();

            int sum = m1Max + m1Min + m2Max + m2Min;

            double perc1Max = 100 * ((double)m1Max) / sum,
                perc1Min = 100 * ((double)m1Min) / sum,
                perc2Max = 100 * ((double)m2Max) / sum,
                perc2Min = 100 * ((double)m2Min) / sum;

            dataGridView1.Rows.Add(m1Max, perc1Max);
            dataGridView1.Rows.Add(m2Max, perc2Max);
            dataGridView1.Rows.Add(m1Min, perc1Min);
            dataGridView1.Rows.Add(m2Min, perc2Min);

            dataGridView1.Rows[0].HeaderCell.Value = "maxM1";
            dataGridView1.Rows[1].HeaderCell.Value = "maxM2";
            dataGridView1.Rows[2].HeaderCell.Value = "minM1";
            dataGridView1.Rows[3].HeaderCell.Value = "minM2";

            dataGridView1.RowHeadersWidthSizeMode = DataGridViewRowHeadersWidthSizeMode.AutoSizeToAllHeaders;
            label1.Text += sum;
        }
    }
}
