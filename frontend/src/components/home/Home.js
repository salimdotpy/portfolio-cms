import About from './About';
import Facts from './Facts';
import Services from './Services';
import Testimonials from './Testimonials';
import AOS  from 'aos';
import 'aos/dist/aos.css';
import { useEffect, useState } from 'react';
import Skills from './Skills';
import Resume from './Resume';
import Contact from './Contact';
// import Portfolio from './components/Portfolio';
import Project from './Project';

function Home() {
  const [setting, setSetting] = useState({});
  useEffect(()=>{
    fetch('http://127.0.0.1:5000/api/1')
    .then(res => res.json())
    .then(setting => setSetting(setting))
    .catch(err => console.error(err));

    AOS.init({
      duration: 1000,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });  
  },[]);
  const hexToRgb = (hex, rgb=true) => {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex)
    if(result){
      return rgb ? `${parseInt(result[1], 16)},${parseInt(result[2], 16)},${parseInt(result[3], 16)}` : hex;
    }
  }
  if(setting){
    document.body.style.setProperty('--primary-color', hexToRgb('#'+setting.base_color, false));
  document.body.style.setProperty('--secondary-color', hexToRgb('#'+setting.secondary_color, false));
  document.body.style.setProperty('--rgb-p-color', hexToRgb('#'+setting.base_color));
  document.body.style.setProperty('--rgb-s-color', hexToRgb('#'+setting.secondary_color));
}
  return (
    <>
    <About/>
    <Facts/>
    <Skills/>
    <Resume/>
    <Project/>
    <Services/>
    <Testimonials/>
    <Contact/>
  </>
  );
}
export default Home;