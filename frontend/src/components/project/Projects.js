import React, { useState, useEffect } from 'react';
import { fetchWithCSRF } from '../Fetch';
import Github from './Github';

function Projects(props) {
    const [project, setProject] = useState(null);
    const [projects, setProjects] = useState(null);
    useEffect(() => {
        fetchWithCSRF('http://localhost:5000/api', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data_keys: 'project.content', singleQuery: 1 })
        })
            .then(res => res.json())
            .then(project => setProject(project.data_values))
            .catch(err => console.error(err));
        fetchWithCSRF('http://localhost:5000/api', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data_keys: 'project.element', orderById: 1 })
        })
            .then(res => res.json())
            .then(projects => setProjects(projects))
            .catch(err => console.error(err));
    }, []);
    let lst = [];
    if (projects) {
        for (let i of projects) {
            lst.push([i.data_values.image_one, i.data_values.title, i.data_values.description, i.data_values.github_link, i.data_values.demo_link, i.data_values.category.toLowerCase()])
        }
    }
    return (
        project && (
        <section id="project" className="project">
            <div className="container">
                <div className="section-title">
                    <h2>{project.heading}</h2>
                    <p>{project.sub_heading}</p>
                </div>
                <div className="row">
                    {lst && lst.map((ele, i) =>
                        <div key={i} className="col-lg-4 col-md-6 mb-lg-0 mb-3 d-flex align-items-stretch pb-4" data-aos="fade-up" data-aos-delay={`${i}00`}>
                            <div className="card  p-3">
                                {ele[5] !== "app"?
                                <>
                                <img src={`http://127.0.0.1:5000/static/assets/images/frontend/project/${ele[0]}`} className='card-img-top' alt=''/>
                                <div className='card-body p-0'>
                                    <h5 className='card-title mt-3'>{ele[1]}</h5>
                                    <p className='card-text' style={{textAlign: 'justify'}}>{ele[2]}</p>
                                    <div className='d-flex justify-content-between'>
                                        <a href={ele[4]} className='btn btn-outline-primary'><i className='las la-globe'></i> Demo</a>
                                        <a href={ele[3]} className='btn btn-primary'><i className='la la-github'></i> GitHub</a>
                                    </div>
                                </div>
                                </> :
                                <>
                                <div className='d-flex flex-row'>
                                    <img src={`http://127.0.0.1:5000/static/assets/images/frontend/project/${ele[0]}`} className='card-img-top align-self-start' alt='' style={{ width: "40%" }} />
                                    <div className='card-body p-0 ps-3'>
                                        <h5 className='card-title'>{ele[1]}</h5>
                                        <p className='card-text' style={{textAlign: 'justify'}}>{ele[2]}</p>
                                    </div>
                                </div>
                                <div className='d-flex justify-content-between pt-3'>
                                    <a href={ele[4]} className='btn btn-outline-primary'><i className='las la-globe'></i> Demo</a>
                                    <a href={ele[3]} className='btn btn-primary'><i className='la la-github'></i> GitHub</a>
                                </div>
                                </>}
                            </div>
                        </div>
                    )}
                </div>
                <Github />
            </div>
        </section>)
    );
}

export default Projects;