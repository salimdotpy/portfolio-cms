import React from 'react';

function Header(props) {
    return (
        <nav id='header' className='navbar shadow fixed-top navbar-light bg-light navbar-expand-lg'>
            <div className='container'>
                <a className='navbar-brand' href='/'>SalimTech</a>
                <button className='navbar-toggler' data-bs-toggle='collapse' data-bs-target='#navbarNav'>
                    <span className='navbar-toggler-icon'></span>
                </button>
                <div className='collapse navbar-collapse' id='navbarNav'>
                    <ul className='navbar-nav ms-auto'>
                        <li className='nav-item'>
                            <a className='nav-link' href='/'>Home</a>
                        </li>
                        <li className='nav-item'>
                            <a className='nav-link' href='/#about'>About</a>
                        </li>
                        <li className='nav-item'>
                            <a className='nav-link' href='/#project'>Project</a>
                        </li>
                        <li className='nav-item'>
                            <a className='nav-link' href='/#services'>Services</a>
                        </li>
                        <li className='nav-item'>
                            <a className='nav-link' href='/#testimonials'>Testimonials</a>
                        </li>
                        <li className='nav-item'>
                            <a className='nav-link' href='/#contact'>Contact</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    );
}

export default Header;