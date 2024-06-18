import React, { useState, useEffect } from 'react';
import { fetchWithCSRF } from '../Fetch';

function About(props) {
    const [about, setAbout] = useState(null);
    const [abouts, setAbouts] = useState(null);
    useEffect(() => {
        fetchWithCSRF('http://localhost:5000/api', {
            method: 'POST',
            body: JSON.stringify({ data_keys: 'about.content', singleQuery: 1 })
        })
        .then(res => res.json())
        .then(about => setAbout(about.data_values))
        .catch(err => console.error(err));

        fetchWithCSRF('http://localhost:5000/api',{
          method: 'POST',
          body: JSON.stringify({ data_keys: 'about.element', orderById: 1 })
        })
      .then(res => res.json())
        .then(abouts => setAbouts(abouts))
        .catch(err => console.error(err));
    }, []);
    let lst = [];
    if(abouts) {
        for(let i of abouts) {
            lst.push([i.data_values.info, i.data_values.value])
        }
    }
    return (
        about && ( 
            <section id="about" className="about">
                <div className="container">

                    <div className="section-title">
                        <h2>{about.heading}</h2>
                        <p>{about.sub_heading}</p>
                    </div>

                    <div className="row">
                        <div className="col-lg-4" data-aos="fade-right">
                            <img src={`http://127.0.0.1:5000/static/assets/images/frontend/about/${about.image}`} className="img-fluid" alt="about-img"/>
                        </div>
                        <div className="col-lg-8 pt-4 pt-lg-0 content" data-aos="fade-left">
                            <h3>{about.skill}</h3>
                            <p className="fst-italic">
                                {about.description}
                            </p>
                            <div className="row">
                                <div className="col-lg-6">
                                    <ul>
                                        {lst && lst.map((ele, i) =>
                                            <li key={i}><i className="bi bi-chevron-right"></i> <strong>{ele[0]}:</strong>
                                                <span>{ele[1]}</span></li>
                                        )}
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>)
    );
}

export default About;