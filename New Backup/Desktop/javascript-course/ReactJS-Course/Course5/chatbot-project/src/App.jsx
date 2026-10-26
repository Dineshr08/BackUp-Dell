//Step3: In code we are removing React from React.useState('') just going to use useState('') beacuse earlier we have imported the package using the script element, now we have installed so just importing itdirectly so no need to use React.useState. While import if we need just specify like import { useState } from 'react' which means we are using useState feature and after from if we use like 'react' which means it will find a package inside node-module inside the react it will look.No need to use ../ and ./ to go inside and outside it will just search inside the node-module for react.Every place removing React.useState or React.useRef to useState.Go to main.jsx for Step4
import { useState } from 'react'

import { ChatInput } from './components/ChatInput';
import { ChatMessages } from './components/ChatMessages';
import {Chatbot} from 'supersimpledev'

//Step7:So vite has the feature where we can directly import the .css or image file directly. Earlier we have learned only we can import js but using vite we can import the css and image files too.So it will load the css for the webiste. We need to keep the images under the assets folder. Directly we can replace the RobotProfileImage, UserProfileImage name in component, as this name referthe full path of the image
import RobotProfileImage from './assets/robot.png'
import UserProfileImage from './assets/user.png'
import './App.css'

//Step1: Commenting the below App and moving our App component and all other components

/*
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}
*/

//Step9: Commenting the components as we are moving into files


// function ChatInput({ chatMessages, setChatMessages }) {
//         const [inputText, setInputText] = useState('');

//         function saveInputText(event) {
//           setInputText(event.target.value);
//         }

//         function sendMessage() {
//           const newChatMessages = [
//             ...chatMessages,
//             {
//               message: inputText,
//               sender: 'user',
//               id: crypto.randomUUID()
//             }
//           ];

//           setChatMessages(newChatMessages);

//           const response = Chatbot.getResponse(inputText);
//           setChatMessages([
//             ...newChatMessages,
//             {
//               message: response,
//               sender: 'robot',
//               id: crypto.randomUUID()
//             }
//           ]);

//           setInputText('');
//         }

//         return (
//           <div className="chat-input-container">
//             <input
//               placeholder="Send a message to Chatbot"
//               size="30"
//               onChange={saveInputText}
//               value={inputText}
//               className="chat-input"
//             />
//             <button
//               onClick={sendMessage}
//               className="send-button"
//             >Send</button>
//           </div>
//         );
//       }

//       function ChatMessage({ message, sender }) {
//         // const message = props.message;
//         // const sender = props.sender;
//         // const { message, sender } = props;

//         /*
//         if (sender === 'robot') {
//           return (
//             <div>
//               <img src="robot.png" width="50" />
//               {message}
//             </div>
//           );
//         }
//         */

//         //Step8:Replacing here using {} as need to subsitue inside jsx need to use {}

//         return (
//           <div className={
//             sender === 'user'
//               ? 'chat-message-user'
//               : 'chat-message-robot'
//           }>
//             {sender === 'robot' && (
//               <img src={RobotProfileImage} className="chat-message-profile" />
//             )}
//             <div className="chat-message-text">
//               {message}
//             </div>
//             {sender === 'user' && (
//               <img src={UserProfileImage} className="chat-message-profile" />
//             )}
//           </div>
//         );
//       }

//       function ChatMessages({ chatMessages }) {
//         const chatMessagesRef = useRef(null);

//         useEffect(() => {
//           const containerElem = chatMessagesRef.current;
//           if (containerElem) {
//             containerElem.scrollTop = containerElem.scrollHeight;
//           }
//         }, [chatMessages]);

//         return (
//           <div className="chat-messages-container" ref={chatMessagesRef}>
//             {chatMessages.map((chatMessage) => {
//               return (
//                 <ChatMessage
//                   message={chatMessage.message}
//                   sender={chatMessage.sender}
//                   key={chatMessage.id}
//                 />
//               );
//             })}
//           </div>
//         );
//       }
      

      function App() {
        const [chatMessages, setChatMessages] = useState([{
          message: 'hello chatbot',
          sender: 'user',
          id: 'id1'
        }, {
          message: 'Hello! How can I help you?',
          sender: 'robot',
          id: 'id2'
        }, {
          message: 'can you get me todays date?',
          sender: 'user',
          id: 'id3'
        }, {
          message: 'Today is September 27',
          sender: 'robot',
          id: 'id4'
        }]);
        // const [chatMessages, setChatMessages] = array;
        // const chatMessages = array[0];
        // const setChatMessages = array[1];

        return (
          <div className="app-container">
            <ChatMessages
              chatMessages={chatMessages}
            />
            <ChatInput
              chatMessages={chatMessages}
              setChatMessages={setChatMessages}
            />
          </div>
        );
      }
    
//Step2: Fixing error
export default App
