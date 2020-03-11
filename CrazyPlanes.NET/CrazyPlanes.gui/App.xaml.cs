using CrazyPlanes.core;
using System.Configuration;
using System.Windows;
using Websockets.core;

namespace CrazyPlanes.gui
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        void AppStartup(object sender, StartupEventArgs e)
        {
            string addresss = ConfigurationManager.AppSettings["address"];
            WebsocketClient websocket = new WebsocketClient(addresss);

            CrazyPlanesGame crazyPlanesGame = new CrazyPlanesGame(websocket);
            crazyPlanesGame.IncomingMessageEvent += CrazyPlanesGame_onIncomingMessage;

            MainWindow mainWindow = new MainWindow(crazyPlanesGame);
            mainWindow.Show();
        }

        private void CrazyPlanesGame_onIncomingMessage(string obj)
        {
            throw new System.NotImplementedException();
        }
    }
}
