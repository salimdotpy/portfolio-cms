import React from 'react';
import { Link } from 'react-router-dom';

function Header(props) {
    return (
        <nav id='header' className='navbar shadow fixed-top navbar-light bg-light navbar-expand-lg'>
            <div className='container'>
                <Link className='navbar-brand' href='/'>SalimTech</Link>
                <button className='navbar-toggler' data-bs-toggle='collapse' data-bs-target='#navbarNav'>
                    <span className='navbar-toggler-icon'></span>
                </button>
                <div className='collapse navbar-collapse' id='navbarNav'>
                    <ul className='navbar-nav ms-auto'>
                        <li className='nav-item'>
                            <Link className='nav-link' to='/'>Home</Link>
                        </li>
                        <li className='nav-item'>
                            <Link className='nav-link' to='/#about'>About</Link>
                        </li>
                        <li className='nav-item'>
                            <Link className='nav-link' to='/#project'>Project</Link>
                        </li>
                        <li className='nav-item'>
                            <Link className='nav-link' to='/#services'>Services</Link>
                        </li>
                        <li className='nav-item'>
                            <Link className='nav-link' to='/#testimonials'>Testimonials</Link>
                        </li>
                        <li className='nav-item'>
                            <Link className='nav-link' to='/#contact'>Contact</Link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    );
}

export default Header;