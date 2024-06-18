import React, { useState } from 'react';
import {Link} from 'react-router-dom';

function SignUp() {
  const [values, setValues] = useState({
    username: '', email: '', password: '', cpassword: '',
  });
  const [errors, setErrors] = useState('');
  const handleChange = (e)=>{
    let partial = {...values, [e.target.id]: e.target.value};
    setValues(partial);
  }
  const handleSubmit = (e)=>{
    e.preventDefault();
    const errors = validate();
    setErrors(errors);
    if(Object.keys(errors).length === 0){
      alert(JSON.stringify(values,null,2));
      reset();
    }
  }
  const validate = ()=>{
    let error = {};
    if(!values.email){
      error.email = "Email is required";
    }else if(!/\S+@\S+\.\S+/.test(values.email)){
      error.email = "Invalid Email format!";
    }
    if(!values.password){
      error.password = "Password is required";
    }else if(values.password.length < 6){
      error.password = "Create strong password";
    }
    if(!values.cpassword){
      error.cpassword = "Confirm the password please";
    }else if(values.password !== values.cpassword){
      error.cpassword = "Both password does not match";
    }
    if(!values.username){
      error.username = "Username is required";
    }else if(values.username.length < 6){
      error.username = "Your name is too small";
    }
    return error;
  }
  function reset(){
    const ret = {...values};
    for(let key in ret){
        ret[key] = '';
    }
    setValues(ret);
  }
  return (
        <div className='card border-primary mb-3' style={{background: 'rgba(255,255,255,.3)'}}>
        <div className='card-body p-5'>
          <form className='' onSubmit={handleSubmit}>
            <h3 className='fw-bolder text-center'>Sign Up</h3>
          <div className='col-md-12'>
            <label htmlFor='username' className='form-label'>Username:</label>
            <input type='text' className='form-control' id='username' placeholder='Enter Username'
            value={values.username} onChange={handleChange}/>
            {errors.username && <div className='text-danger'>{errors.username}</div>}
          </div>
          <div className='col-md-12'>
            <label htmlFor='email' className='form-label'>Email:</label>
            <input type='text' className='form-control' id='email' placeholder='Enter Email'
            value={values.email} onChange={handleChange}/>
            {errors.email && <div className='text-danger'>{errors.email}</div>}
          </div>
          <div className='form-group mt-3'>
            <label htmlFor='password' className='form-label'>Password:</label>
            <input type='password' className='form-control' id='password' placeholder='Enter Password'
            value={values.password} onChange={handleChange}/>
            {errors.password && <span className='text-danger'>{errors.password}</span>}
          </div>
          <div className='form-group mt-3'>
            <label htmlFor='cpassword' className='form-label'>Confirm Password:</label>
            <input type='password' className='form-control' id='cpassword' placeholder='Confirm Password'
            value={values.cpassword} onChange={handleChange}/>
            {errors.cpassword && <span className='text-danger'>{errors.cpassword}</span>}
          </div>
          <div className='form-group mt-4'>
            <button className='btn btn-primary w-100'>Sign Up</button>
          </div>
          <div className='form-group mt-4'>
            <button type='button' onClick={()=>{setErrors(''); reset();}} 
            className='btn btn-danger float-start'>Reset</button>
            <Link to={'/login'} className='btn btn-outline-info float-end'>or Login</Link>
          </div>
        </form>
        </div>
      </div>
  );
}

export default SignUp;