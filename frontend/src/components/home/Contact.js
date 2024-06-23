import React, { useState, useEffect } from 'react';
import { fetchWithCSRF } from '../Fetch';

function Contact(props) {
    const [contact, setContact] = useState(null);
    useEffect(() => {
        fetchWithCSRF('api', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data_keys: 'contact.content', singleQuery: 1 })
        })
            .then(res => res.json())
            .then(contact => setContact(contact.data_values))
            .catch(err => console.error(err));
    }, []);
    return (
        contact && (
            <section id="contact" className="contact">
                <div className="container">
                    <div className="section-title">
                        <h2>{contact.heading}</h2>
                        <p>{contact.sub_heading}</p>
                    </div>
                    <div className="row" data-aos="fade-in">
                        <div className="col-lg-5 d-flex align-items-stretch">
                            <div className="info">
                                <div className="address">
                                    <i className="bi bi-geo-alt"></i>
                                    <h4>Location:</h4>
                                    <p>{contact.location}</p>
                                </div>
                                <div className="email">
                                    <i className="bi bi-envelope"></i>
                                    <h4>Email:</h4>
                                    <p>{contact.email}</p>
                                </div>
                                <div className="phone">
                                    <i className="bi bi-phone"></i>
                                    <h4>Call:</h4>
                                    <p>{contact.phone}</p>
                                </div>
                                <iframe
                                    src={contact.map_source}
                                    title={contact.sub_heading}
                                    style={{border:0, width: '100%', height: '290px'}} allowFullScreen></iframe>
                            </div>
                        </div>
                        <div className="col-lg-7 mt-5 mt-lg-0 d-flex align-items-stretch">
                            <form action="/" method="post" className="php-email-form">
                                <div className="row">
                                    <div className="form-group col-md-6">
                                        <label htmlFor="name">Your Name</label>
                                        <input type="text" name="name" className="form-control" id="name" required />
                                    </div>
                                    <div className="form-group col-md-6">
                                        <label htmlFor="email">Your Email</label>
                                        <input type="email" className="form-control" name="email" id="email" required/>
                                    </div>
                                </div>
                                <div className="form-group">
                                    <label htmlFor="subject">Subject</label>
                                    <input type="text" className="form-control" name="subject" id="subject" required/>
                                </div>
                                <div className="form-group">
                                    <label htmlFor="message">Message</label>
                                    <textarea className="form-control" name="message" id="message" rows="10"
                                        required></textarea>
                                </div>
                                <div className="my-3">
                                    <div className="loading">Loading...</div>
                                    <div className="error-message"></div>
                                    <div className="sent-message">Your message has been sent. Thank you!</div>
                                </div>
                                <div className="text-center"><button type="submit">{contact.button_text}</button></div>
                            </form>
                        </div>
                    </div>
                </div>
            </section>)
    );
}

export default Contact;