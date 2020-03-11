using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Websockets.core;

namespace CrazyPlanes.core
{
    public class CrazyPlanesGame
    {
        private readonly IWebsocketClient _websocket;
        private bool _isDone;

        public CrazyPlanesGame(IWebsocketClient websocket)
        {
            _websocket = websocket;
        }

        public event Action<string> IncomingMessageEvent;
        
        public void SetSize(int width, int height)
        {

            _websocket.Send(
                JsonConvert.SerializeObject(
                    new Dictionary<string, int> {
                        { "width", width },
                        { "height", height }
                    }
                )
            );
        }

        public void SetPlanes(IPlane[] planes)
        {
            _websocket.Send(
                JsonConvert.SerializeObject(planes)
            );
        }

        public void RunGame()
        {
            _websocket.Send("start");
            _isDone = true;

            do
            {
                IncomingMessageEvent?.Invoke(_websocket.Receive());
            }
            while (!_isDone);
        }

        public void StopGame()
        {
            _isDone = false;
        }
    }
}
