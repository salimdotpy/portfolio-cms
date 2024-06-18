import React, { useRef, useEffect } from 'react';

function Footer(props) {
    const toTopRef = useRef(null);
    useEffect(() => {
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
                        <a href="/" className="twitter"><i className="bx bxl-twitter"></i></a>
                        <a href="/" className="facebook"><i className="bx bxl-facebook"></i></a>
                        <a href="/" className="instagram"><i className="bx bxl-instagram"></i></a>
                        <a href="/" className="google-plus"><i className="bx bxl-skype"></i></a>
                        <a href="/" className="linkedin"><i className="bx bxl-linkedin"></i></a>
                    </div>
                </div>
            </footer>
            <a href="/#" ref={toTopRef} className="back-to-top d-flex align-items-center justify-content-center"><i
                className="bi bi-arrow-up-short"></i></a>
        </>
    );
}

export default Footer;