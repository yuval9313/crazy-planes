using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace CrazyPlanes.gui.Pages
{
    /// <summary>
    /// Interaction logic for IntroPage.xaml
    /// </summary>
    public partial class IntroPage : Page
    {
        public IntroPage()
        {
            InitializeComponent();
        }

        public event Action<int, int> SubmitEvent;

        private void OnSubmitClick(object sender, RoutedEventArgs e)
        {
            int height = int.Parse(this._heightBox.Text);
            int width = int.Parse(this._widthBox.Text);
            SubmitEvent?.Invoke(width, height);
        }

        private void TextBoxNumbersOnly(object sender, TextCompositionEventArgs e)
        {
            e.Handled = Utils.IsTextOnly(e.Text);
        }
    }
}
