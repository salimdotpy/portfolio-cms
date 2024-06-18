import React, { useState, useEffect } from 'react';
import ProgressBar from './ProgressBar';
import { fetchWithCSRF } from '../Fetch';

function Skills(props) {
    const [skill, setSkill] = useState(null);
    const [skills, setSkills] = useState(null);
    useEffect(() => {
        fetchWithCSRF('http://localhost:5000/api', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data_keys: 'skills.content', singleQuery: 1 })
        })
            .then(res => res.json())
            .then(skill => setSkill(skill.data_values))
            .catch(err => console.error(err));
        fetchWithCSRF('http://localhost:5000/api', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data_keys: 'skills.element', orderById: 1 })
        })
            .then(res => res.json())
            .then(skills => setSkills(skills))
            .catch(err => console.error(err));
    }, []);
    let lst = [];
    if (skills) {
        for (let i of skills) {
            lst.push([i.data_values.skill, i.data_values.skill_level, i.data_values.skill])
        }
    }
    return (
        skill && (
            <section id="skills" className="skills">
                <div className="container">
                    <div className="section-title">
                        <h2>{skill.heading}</h2>
                        <p>{skill.sub_heading}</p>
                    </div>
                    <div className="row skills-content">
                        {lst && lst.map((ele, i) =>
                            <div key={i} className="col-lg-6" data-aos="fade-up" data-aos-delay={`${i}00`}>
                                <div className="progress">
                                    <span className="skill">{ele[0]} <i className="val">{ele[1]}%</i></span>
                                    <div className="progress-bar-wrap">
                                        <ProgressBar min={0} val={ele[1]}/>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            </section>)
    );
}

export default Skills;