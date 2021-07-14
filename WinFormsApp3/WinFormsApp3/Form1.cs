using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;
using System.Threading;
namespace WinFormsApp3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            this.TopMost = true;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
           
            Process ps = new Process();
            string yourURL = "/K cd /d D:\\jacob_liang\\Desktop & python 1.py";
            ps.StartInfo.FileName = "cmd.exe";
            ps.StartInfo.CreateNoWindow = true;
            ps.StartInfo.Arguments = yourURL;
            ps.Start();

            Process ps2 = new Process();
            string yourURL2 = "/K cd /d D:\\jacob_liang\\Desktop & python 2.py";
            ps2.StartInfo.FileName = "cmd.exe";
            ps2.StartInfo.CreateNoWindow = true;
            ps2.StartInfo.Arguments = yourURL2;
            ps2.Start();
           
            // Application.Exit();

        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*foreach (System.Diagnostics.Process oItem in System.Diagnostics.Process.GetProcesses())
            {
                string cID = "";    //執行續ID
                string cPN = "";    //執行檔名稱
                string cFD = "";    //執行檔描述
                try
                {
                    cID = oItem.Id.ToString();
                    cPN = oItem.ProcessName;
                    cFD = oItem.MainModule.FileVersionInfo.FileDescription;
                }
                catch
                {
                    //Access Denied
                }
                MessageBox.Show($"PID: {cID}\nFileName: {cPN}\nFileDescription: {cFD}\n---");
            }
            */
           
          
                Process[] processes = Process.GetProcessesByName("cmd");

                foreach (Process app in processes)
                {
                    //  MessageBox.Show("cmd");
                    // 先等待 1000 毫秒
                    app.WaitForExit(10);

                    // 關閉應用程序
                    app.CloseMainWindow();

                    // 釋放資源
                    app.Close();
                }



                Process[] processes2 = Process.GetProcessesByName("python");

                foreach (Process app2 in processes2)
                {
                    //  MessageBox.Show("python");
                    // 先等待 1000 毫秒
                    app2.WaitForExit(10);

                    // 關閉應用程序
                    app2.CloseMainWindow();

                    // 釋放資源
                    app2.Close();
                }

            





            Application.Exit();


        }
    }
}
