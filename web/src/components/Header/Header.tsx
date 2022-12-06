import DoubleWaves from './DoubleWaves'
import Scrolldown from './Scrolldown'

import './Header.css'

const Header = () => {
  return (
    <section className='header' id='header'>
        
        <div>
          <h1 className='title'>A NLP-based multilingual discord chatbot</h1>
          <article className='desc'>Celestial, a NLP-based discord chatbot who could talk to you in Thai and English</article>
        </div> 

        <Scrolldown />

    </section>
  )
}

export default Header