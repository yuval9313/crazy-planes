using System;
using System.Linq;
using System.Net.WebSockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Websockets.core
{
    public class WebsocketClient : IWebsocketClient
    {
        private readonly ClientWebSocket _clientSocket;

        public WebsocketClient(string address)
        {
            var uri = new Uri(address);
            _clientSocket = new ClientWebSocket();
            _clientSocket.ConnectAsync(uri, CancellationToken.None);
        }

        public async void Send(string message)
        {
            ArraySegment<byte> buffer = new ArraySegment<byte>(Encoding.UTF8.GetBytes(message));
            await _clientSocket.SendAsync(buffer, WebSocketMessageType.Text, true, CancellationToken.None);
        }

        public string Receive()
        {
            return new Lazy<Task<string>>(async () =>
            {
                var lengthBuffer = new ArraySegment<byte>(new byte[4]);
                var _ = await _clientSocket.ReceiveAsync(lengthBuffer, CancellationToken.None);
                byte[] lenBuf;
                if (BitConverter.IsLittleEndian)
                {
                    lenBuf = (lengthBuffer.Array ?? throw new NullReferenceException()).Reverse().ToArray();
                }
                else
                    lenBuf = lengthBuffer.Array;
                var len = BitConverter.ToUInt32(lenBuf ?? throw new NullReferenceException(), 0);
                Console.WriteLine(len);
                var buffer = new ArraySegment<byte>(new byte[(int)len]);
                var result = await _clientSocket.ReceiveAsync(buffer, CancellationToken.None);
                return Encoding.UTF8.GetString(buffer.Array ?? throw new NullReferenceException(), 0, result.Count);
            }).Value.Result;
        }
    }
}
