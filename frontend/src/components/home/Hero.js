import React, { useState, useEffect} from 'react';
import Typewriter from "typewriter-effect";
import { fetchWithCSRF } from '../Fetch';

function Hero(props) {
    const [hero, setHero] = useState(null);
    useEffect(()=>{
        fetchWithCSRF('api', {
            method: 'post',
            headers:{'Content-Type': 'application/json'},
            body: JSON.stringify({data_keys: 'hero.content', singleQuery: 1})
        })
        .then(res => res.json())
        .then(hero=>setHero(hero.data_values))
        .catch(err => console.error(err));
    },[]);
    const Type = ()=> {
        return (
            hero && (<Typewriter
            options={{
              strings: hero.keywords,
              autoStart: true,
              loop: true,
              deleteSpeed: 50,
            }}
          />
        ));
      }
    return (
        hero && (
        <section id='hero' className='d-flex flex-column justify-content-center align-items-center' style={{backgroundImage: "url(https://salimtech.pythonanywhere.com/static/assets/images/frontend/hero/"+hero.image+")"}}>
            <div className='hero-container' data-aos="fade-in">
                <h2>Hi there, I'm</h2>
                <h1>Selim Adekola</h1>
                {/* {hero? <h1>{hero.name}</h1> : <h1>Selim Adekola</h1>}  */}
                <div>I'm <Type/></div>
            </div>
        </section>
        )
    );
}

export default Hero;