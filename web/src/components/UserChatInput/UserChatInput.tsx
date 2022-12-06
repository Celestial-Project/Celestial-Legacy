import { useState } from 'react'
import get_response from '../../../API/get_response'

import Waves from '../../assets/layered-waves-haikei.svg'

import './UserChatInput.css'

const UserChatInput = (): JSX.Element => {
    
    const [text, setText] = useState('-- Please submit a input --')
    const [input, setInput] = useState('')
    
    const handleChat = async () => {
        setText(await get_response(input))
    }
  
    return (
        <section className="user-demo -mt-16">

            <img src={Waves} alt="waves" className='rotate-180 scroll mix-blend-lighten max-md:-mt-1'/>

            <h1 className="text-6xl font-semibold mt-32" id='demo'>Live demo</h1>
            <h3 className="text-base mt-3.5">Try the live demo of our chatbot here!</h3>

            <div className=" flex flex-col gap-4 mt-10">

                <p className="text-base">{text}</p>
                
                <textarea 
                    id="userInput" 
                    name="userInput" 
                    rows={1}
                    className="block p-3 mx-14 min-w-max text-sm rounded-lg border border-gray-300"
                    value={input}
                    placeholder="Say someting to Celestial-chan here!"
                    onChange={(e) => setInput(e.target.value)}
                >
                </textarea>

                <button onClick={handleChat} className="text-white bg-[#464646] hover:bg-[#242424] hover:border-white focus:outline-none focus:ring-4 focus:ring-gray-300 font-medium rounded-xl text-sm px-5 py-2.5 mx-14">Press me!</button>

            </div>

        </section>
    )
}

export default UserChatInput