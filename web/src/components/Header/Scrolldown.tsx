import { FaArrowDown } from 'react-icons/fa'
import Waves from '../../assets/layered-waves-haikei.svg'

const Scrolldown = () => {
  return (

    <div className='mt-28'>

        <div className='container pt-5 pb-1 px-10 mx-0 min-w-full flex flex-col items-center mt-28 z-1 absolute'>
            <a href='#demo' className='p-8'>
                <FaArrowDown className='bg-[#464646] h-12 w-12 p-2 rounded-full'/>
            </a>
        </div>

        <img src={Waves} alt='waves' className='waves z-0' />

    </div>
  )
}

export default Scrolldown