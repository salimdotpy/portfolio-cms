import React, { useState, useEffect } from 'react';
import Counter from './Counter';
import { fetchWithCSRF } from '../Fetch';

function Facts(props) {
    const [fact, setFact] = useState(null);
    const [facts, setFacts] = useState(null);
    useEffect(() => {
        fetchWithCSRF('api', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data_keys: 'facts.content', singleQuery: 1 })
        })
            .then(res => res.json())
            .then(fact => setFact(fact.data_values))
            .catch(err => console.error(err));
        fetchWithCSRF('api', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data_keys: 'facts.element', orderById: 1 })
        })
            .then(res => res.json())
            .then(facts => setFacts(facts))
            .catch(err => console.error(err));
    }, []);
    let lst = [];
    if (facts) {
        for (let i of facts) {
            const txt = {__html:i.data_values.icon};
            lst.push([txt, i.data_values.count, i.data_values.fact])
        }
    }
    return (
        fact && (
            <section id="facts" className="facts">
                <div className="container">
                    <div className="section-title">
                        <h2>{fact.heading}</h2>
                        <p>{fact.sub_heading}</p>
                    </div>
                    <div className="row no-gutters">
                        {lst && lst.map((ele, i) =>
                            <div key={i} className="col-lg-3 col-md-6 d-md-flex align-items-md-stretch" data-aos="fade-up" data-aos-delay={`${i}00`}>
                                <div className="count-box">
                                    <code dangerouslySetInnerHTML={ele[0]}></code>
                                    <Counter start={0} stop={ele[1]} duration={1} className="purecounter"/>
                                    <p><strong>{ele[2]}</strong></p>
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            </section>)
    );
}

export default Facts;