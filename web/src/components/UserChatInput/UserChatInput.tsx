import { useState } from 'react'
import get_response from '../../../API/get_response'

import './UserChatInput.css'

const UserChatInput = () => {
    
    const [text, setText] = useState('-- Please submit a input --')
    const [input, setInput] = useState('')
    
    const handleChat = async () => {
        setText(await get_response(input))
    }
  
    return (
        <div className="user-demo">

            <h1>Live demo</h1>
            <h3>Try the live demo of our chatbot here!</h3>

            <div className="user-chat-container">

                <p className="response-text">{text}</p>
                
                <textarea 
                    id="userInput" 
                    name="userInput" 
                    className="user-input"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    ></textarea>

                <button onClick={handleChat} className="btn-submit">Press me!</button>

            </div>

        </div>
    )
}

export default UserChatInput