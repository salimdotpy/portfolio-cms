import React, { useState, useEffect } from 'react';
import { Swiper, SwiperSlide } from "swiper/react";
import { Pagination, Autoplay} from "swiper/modules";

import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/autoplay";
import { fetchWithCSRF } from '../Fetch';

function Testimonials(props) {
    const [testimonial, setTestimonial] = useState(null);
    const [testimonials, setTestimonials] = useState(null);
    useEffect(() => {
        fetchWithCSRF('api', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data_keys: 'testimonials.content', singleQuery: 1 })
        })
            .then(res => res.json())
            .then(testimonial => setTestimonial(testimonial.data_values))
            .catch(err => console.error(err));
        fetchWithCSRF('api', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data_keys: 'testimonials.element', orderById: 1 })
        })
            .then(res => res.json())
            .then(testimonials => setTestimonials(testimonials))
            .catch(err => console.error(err));
    }, []);
    let lst = [];
    if (testimonials) {
        for (let i of testimonials) {
            lst.push([i.data_values.say, i.data_values.image, i.data_values.name, i.data_values.designation]);
        }
    }
    return (
        testimonial && (
            <section id="testimonials" className="testimonials">
                <div className="container">
                    <div className="section-title">
                        <h2>{testimonial.heading}</h2>
                        <p>{testimonial.sub_heading}</p>
                    </div>
                    <Swiper modules={[Pagination, Autoplay]}
                        className='.testimonials-slider' speed={400} 
                        autoplay={{ delay: 5000, disableOnInteraction: false }} slidesPerView={'auto'}
                        breakpoints={{
                            320: { slidesPerView: 1, spaceBetween: 20 },
                            700: { slidesPerView: 2, spaceBetween: 20 },
                            1200: { slidesPerView: 3, spaceBetween: 20 }
                        }} pagination={{
                            type: 'bullets',
                            clickable: true
                        }} data-aos="fade-up" data-aos-delay="100">
                        {lst && lst.map((ele, index) =>
                            <SwiperSlide key={index} className='swiper-slide'>
                                <div className="testimonial-item" data-aos="fade-up" data-aos-delay={`${index}00`}>
                                    <p><i className="bx bxs-quote-alt-left quote-icon-left"></i>
                                        {ele[0]}
                                        <i className="bx bxs-quote-alt-right quote-icon-right"></i>
                                    </p>
                                    <img src={`https://salimtech.pythonanywhere.com/static/assets/images/frontend/testimonials/${ele[1]}`} className="testimonial-img" alt="" />
                                    <h3>{ele[2]}</h3>
                                    <h4>{ele[3]}</h4>
                                </div>
                            </SwiperSlide>
                        )}
                    </Swiper>
                </div>
            </section>
        )
    );
}

export default Testimonials;