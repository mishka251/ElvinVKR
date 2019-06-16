using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
namespace ElvinVKR
{
    class portfel
    {
        List<string> akcii;
        List<int> percs;
        double m1, m2, dohod;

        public portfel()
        {

        }

        public portfel(List<string> akcii, List<int> percs, double m1, double m2, double dohod)
        {
            this.akcii = akcii ?? throw new ArgumentNullException(nameof(akcii));
            this.percs = percs ?? throw new ArgumentNullException(nameof(percs));
            this.m1 = m1;
            this.m2 = m2;
            this.dohod = dohod;
        }

        public void Save(StreamWriter sw)
        {
            sw.WriteLine($"{ String.Join(",", this.akcii)}");
            sw.WriteLine($"{ String.Join(",", this.percs)}");
            sw.WriteLine($"{m1} {m2} {dohod}");
        }

        public static portfel Load(StreamReader sr)
        {
            portfel p = new portfel();

            string s = sr.ReadLine();
            p.akcii = s.Split(',').ToList();

            s = sr.ReadLine();
            p.percs = s.Split(',').ToList().Select( s1 => int.Parse(s1)).ToList();

            s = sr.ReadLine();
            var s_arr = s.Split(' ');
            p.m1 = double.Parse(s_arr[0]);
            p.m2 = double.Parse(s_arr[1]);
            p.dohod = double.Parse(s_arr[2]);

            return p;
        }

        public object[] toArr()
        {
            return new
            object[]{ String.Join(", ", this.akcii), String.Join(", ", this.percs), Math.Round(this.m1, 2), Math.Round(this.m2,2), Math.Round(100* this.dohod, 2)+"%"};
        }

        public static bool operator >(portfel p1, portfel p2) => p1.dohod > p2.dohod;
        public static bool operator <(portfel p1, portfel p2) => p1.dohod < p2.dohod;

        public static bool operator >=(portfel p1, portfel p2) => p1.dohod >= p2.dohod;

        public static bool operator <=(portfel p1, portfel p2) => p1.dohod <= p2.dohod;

        public static bool operator ==(portfel p1, portfel p2) => p1.dohod == p2.dohod;
        public static bool operator !=(portfel p1, portfel p2) => p1.dohod != p2.dohod;

    }
}
