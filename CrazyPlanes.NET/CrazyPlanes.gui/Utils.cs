using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace CrazyPlanes.gui
{
    public static class Utils
    {
        public static readonly Regex _numeralRegex = new Regex("[0-9]+"); //regex that matches disallowed text
        public static bool IsTextOnly(string text)
        {
            return !_numeralRegex.IsMatch(text);
        }
    }
}
