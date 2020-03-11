namespace Websockets.core
{
    public interface IWebsocketClient
    {
        string Receive();
        void Send(string message);
    }
}