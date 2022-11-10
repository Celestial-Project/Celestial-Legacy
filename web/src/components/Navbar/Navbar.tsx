import { useState } from 'react'

import './Navbar.css'

const Navbar = () => {

    const [click, setClick] = useState(false)

  return (
    <>
        <nav>

            <img 
                src="https://cdn.discordapp.com/app-icons/927573556961869825/b4b624c1cb68fa3a99a24a8e9942d2a5.png" 
                alt="image" 
                className='logo'
            />

            <div className="nav-container">

                <ul className={click ? 'nav-list-active' : 'nav-list'}>

                    <li>
                        <a href="#header">Home</a>
                    </li>
                    
                    <li>
                        <a href="#demo">Live demo</a>
                    </li>

                </ul>

            </div>

            <div className="nav-moblie" onClick={() => setClick(!click)}>
                <i className={ click ? 'fas fa-times' : 'fas fa-bars'}></i>
            </div>

        </nav>
    </>
  )
}

export default Navbar