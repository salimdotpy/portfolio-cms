import React, { useRef, useEffect, useState } from 'react';
import { fetchWithCSRF } from './Fetch';
import { Link } from 'react-router-dom';

function Footer(props) {
    const toTopRef = useRef(null);
    const [footer, setFooter] = useState(null);
    useEffect(() => {
        fetchWithCSRF('api', {
            method: 'POST',
            body: JSON.stringify({ data_keys: 'footer.element', orderById: 1 })
        })
        .then(res => res.json())
        .then(footer => setFooter(footer))
        .catch(err => console.error(err));

        const toggleBacktotop = () => {
            if (window.scrollY > 100) {
                toTopRef.current.classList.add('active')
            } else {
                toTopRef.current.classList.remove('active')
            }
        }
        window.addEventListener('load', toggleBacktotop)
        document.addEventListener('scroll', toggleBacktotop)

    }, [toTopRef]);
    
    let lst = [];
    if (footer) {
        for (let i of footer) {
            const txt = {__html:i.data_values.social_icon};
            lst.push([i.data_values.social_link, i.data_values.social_name, txt])
        }
    }
    return (
        <>
            <footer id="footer">
                <div className="container d-md-flex py-4">
                    <div className="me-md-auto text-center text-md-start">
                        <div className="copyright">
                            &copy; Copyright <strong><span>SalimTech</span></strong>. All Rights Reserved
                        </div>
                    </div>
                    <div className="social-links text-center text-md-right pt-3 pt-md-0">
                        {lst && lst.map((ele, i) =>
                        <Link key={i} target='_blank' to={ele[0]} className={ele[1]}>
                            <code dangerouslySetInnerHTML={ele[2]}></code>
                        </Link>
                        )}
                    </div>
                </div>
            </footer> 
            <a href="/#" ref={toTopRef} className="back-to-top d-flex align-items-center justify-content-center"><i
                className="bi bi-arrow-up-short"></i></a>
        </>
    );
}

export default Footer;