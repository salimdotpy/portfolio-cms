import React, { useState, useEffect } from 'react';
import { fetchWithCSRF } from '../Fetch';

function Services(props) {
    const [service, setService] = useState(null);
    const [services, setServices] = useState(null);
    useEffect(() => {
        fetchWithCSRF('http://localhost:5000/api', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data_keys: 'services.content', singleQuery: 1 })
        })
            .then(res => res.json())
            .then(service => setService(service.data_values))
            .catch(err => console.error(err));
        fetchWithCSRF('http://localhost:5000/api', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data_keys: 'services.element', orderById: 1 })
        })
            .then(res => res.json())
            .then(services => setServices(services))
            .catch(err => console.error(err));
    }, []);
    let lst = [];
    if (services) {
        for (let i of services) {
            lst.push([i.data_values.icon, i.data_values.title, i.data_values.description])
        }
    }
    return (
        service && (
            <section id="services" className="services">
                <div className="container">
                    <div className="section-title">
                        <h2>{service.heading}</h2>
                        <p>{service.sub_heading}</p>
                    </div>
                    <div className="row">
                        {lst && lst.map((ele, i) =>
                            <div key={i} className="col-lg-4 col-md-6 icon-box" data-aos="fade-up" data-aos-delay={`${i}00`}>
                                <div className="icon" dangerouslySetInnerHTML={{__html:ele[0]}}></div>
                                <h4 className="title"><a href="/">{ele[1]}</a></h4>
                                <p className="description">{ele[2]}</p>
                            </div>
                        )}
                    </div>
                </div>
            </section>)
    );
}

export default Services;
