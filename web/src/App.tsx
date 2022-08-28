// import './App.css'
import { useState } from 'react'
import get_response from '../API/get_response'

function App() {

  const [text, setText] = useState('')

  const handleBtn = async () => {
    setText(await get_response("a"))
  }

  return (
    <div className="App">
      <h1>Hello, world!</h1>
      <h3>{text}</h3>
      <button onClick={handleBtn}>Click me</button>
    </div>
  )
}

export default App
