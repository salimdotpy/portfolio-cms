import React, { useState, useEffect } from 'react';
import { fetchWithCSRF } from '../Fetch';

function Resume(props) {
    const [resume, setResume] = useState(null);
    const [resumes, setResumes] = useState(null);
    useEffect(() => {
        fetchWithCSRF('http://localhost:5000/api', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data_keys: 'resume.content', singleQuery: 1 })
        })
            .then(res => res.json())
            .then(resume => setResume(resume.data_values))
            .catch(err => console.error(err));
        fetchWithCSRF('http://localhost:5000/api', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data_keys: 'resume.element', orderById: 1 })
        })
            .then(res => res.json())
            .then(resumes => setResumes(resumes))
            .catch(err => console.error(err));
    }, []);
    let lst = [];
    if (resumes) {
        for (let i of resumes) {
            lst.push([i.data_values.resume_title, i.data_values.resume_item])
        }
    }
    return (
        resume && (
            <section id="resume" className="resume">
                <div className="container">
                    <div className="section-title">
                        <h2>{resume.heading}</h2>
                        <p>{resume.sub_heading}</p>
                    </div>
                    <div className="row">
                        <div className="col-lg-6" data-aos="fade-up" data-aos-delay={`200`}>
                        {lst && lst.map((ele, i) =>
                        i<2?
                            (<span key={i}>
                                <h3 className="resume-title">{ele[0]}</h3>
                                <div className='' dangerouslySetInnerHTML={{__html:ele[1]}}></div>
                            </span>):''
                        )}
                        </div>
                        {lst && lst.map((ele, i) =>
                        i>=2?
                            (<div key={i} className="col-lg-6" data-aos="fade-up" data-aos-delay={`${i+1}00`}>
                                <h3 className="resume-title">{ele[0]}</h3>
                                <div className='' dangerouslySetInnerHTML={{__html:ele[1]}}></div>
                            </div>):''
                        )}
                    </div>
                </div>
            </section>)
    );
}

export default Resume;