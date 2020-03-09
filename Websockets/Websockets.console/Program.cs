using System;
using Websockets.core;

namespace Websockets.console
{
    internal static class Program
    {
        private static void Main(string[] args)
        {
            var websocketClient = new WebsocketClient("ws://localhost:5000");
            while (true)
            {
                Console.WriteLine("Enter a message: ");
                var message = Console.ReadLine();
                websocketClient.Send(message);
                Console.WriteLine(websocketClient.Receive());
            }
        }
    }
}