import React, { useState } from 'react';
import {Link} from 'react-router-dom';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState('');
  const handleSubmit = (e)=>{
    e.preventDefault();
    const errors = validate();
    setErrors(errors);
    if(Object.keys(errors).length === 0){
      alert('Youve successfully logged in!');
      setEmail(''); setPassword('');
    }
  }
  const validate = ()=>{
    let error = {};
    if(!email){
      error.email = "Email is required";
    }else if(!/\S+@\S+\.\S+/.test(email)){
      error.email = "Invalid Email format!";
    }
    if(!password){
      error.password = "Password is required";
    }else if(password.length < 6){
      error.password = "Create strong password";
    }
    return error;
  }
  return (
        <div className='card border-primary mb-3' style={{background: 'rgba(255,255,255,.3)'}}>
        <div className='card-body p-5'>
          <form className='' onSubmit={handleSubmit}>
            <h3 className='fw-bolder text-center'>Login Now!</h3>
          <div className='col-md-12'>
            <label htmlFor='email' className='form-label'>Email:</label>
            <input type='text' className='form-control' id='email' placeholder='Enter Email'
            value={email} onChange={(e)=>setEmail(e.target.value)}/>
            {errors.email && <div className='text-danger'>{errors.email}</div>}
          </div>
          <div className='form-group mt-3'>
            <label htmlFor='password' className='form-label'>Password:</label>
            <input type='password' className='form-control' id='password' placeholder='Enter Password'
            value={password} onChange={(e)=>setPassword(e.target.value)}/>
            {errors.password && <span className='text-danger'>{errors.password}</span>}
          </div>
          <div className='form-check mt-3'>
            <input type='checkbox' className='form-check-input' id='rem'/>
            <label htmlFor='rem' className='form-check-label'>Remember me</label>
            <Link to={'/'} className='float-end text-decoration-none'>Forgot Password?</Link>
          </div>
          <div className='form-group mt-4'>
            <button className='btn btn-primary w-100'>Login</button>
          </div>
          <div className='form-group mt-4'>
            <button type='button' onClick={()=>{setEmail(''); setPassword(''); setErrors('');}} 
            className='btn btn-danger float-start'>Reset</button>
            <Link to={'/signup'} className='btn btn-outline-info float-end'>or Sign up</Link>
          </div>
        </form>
        </div>
      </div>
  );
}

export default Login;