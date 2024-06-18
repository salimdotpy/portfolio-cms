import React, { useState, useEffect } from 'react';
import { fetchWithCSRF } from '../Fetch';

function Portfolio(props) {
    const [portfolio, setPortfolio] = useState(null);
    const [portfolios, setPortfolios] = useState(null);
    useEffect(() => {
        fetchWithCSRF('http://localhost:5000/api', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data_keys: 'portfolio.content', singleQuery: 1 })
        })
            .then(res => res.json())
            .then(portfolio => setPortfolio(portfolio.data_values))
            .catch(err => console.error(err));
        fetchWithCSRF('http://localhost:5000/api', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data_keys: 'portfolio.element', orderById: 1 })
        })
            .then(res => res.json())
            .then(portfolios => setPortfolios(portfolios))
            .catch(err => console.error(err));
    }, []);
    let lst = [];
    if (portfolios) {
        for (let i of portfolios) {
            lst.push([i.data_values.image_one, i.data_values.portfolio_category])
        }
    }
    return (
        portfolio && (
            <section id="portfolio" className="portfolio">
                <div className="container">
                    <div className="section-title">
                        <h2>{portfolio.heading}</h2>
                        <p>{portfolio.sub_heading}</p>
                    </div>
                    <div className="row">
                        {lst && lst.map((ele, i) =>
                            <div key={i} className="col-lg-3 col-md-6 mb-lg-0 mb-3 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay={`${i}00`}>
                                <div className="card">
                                    <img src={`http://127.0.0.1:5000/static/assets/images/frontend/portfolio/${ele[0]}`} className='card-img-top' alt='' style={{ height: "270px", width: "100%" }} />
                                    <div className='card-body'>
                                        <h5 className='card-title'>{ele[1]}</h5>
                                        <p className='card-text'>{ele[0]}</p>
                                        <div className='d-flex justify-content-between'>
                                            <a href='/' className='btn btn-outline-primary btn-sm'><i className='las la-globe'></i> Demo</a>
                                            <a href='/' className='btn btn-primary btn-sm'><i className='la la-github'></i> GitHub</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )}
                        <div className='d-flex mt-4 justify-content-center align-items-center'>
                            <a href='/' className='btn btn-outline-info btn-lg shadow px-5 rounded-pill'>More <i className='la la-arrow-circle-right'></i></a>
                        </div>
                    </div>
                </div>
            </section>)
    );
}

export default Portfolio;