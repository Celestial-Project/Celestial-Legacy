import Waves from '../../assets/layered-waves-haikei.svg'

const DoubleWaves = () => {
  return (
    <>
        <img src={Waves} alt='waves' className='waves' />
        <img src={Waves} alt='waves' className='rotate-180 -mt-10 mix-blend-lighten max-md:-mt-1'/>
    </>
  )
}

export default DoubleWaves