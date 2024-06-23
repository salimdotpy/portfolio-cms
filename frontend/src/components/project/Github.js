import React, { useEffect, useState } from 'react';
import GitHubCalendar from "react-github-calendar";

function Github() {
  const [color, setColor] = useState({});
  useEffect(()=>{
    fetch('https://salimtech.pythonanywhere.com/api/1')
    .then(res => res.json())
    .then(color => setColor(color.base_color))
    .catch(err => console.error(err));
 
  },[]);
  return (
    <div className="row justify-content-center py-3">
      <h4 className="project-heading pb-2">
        Days I <strong className="purple">Code</strong>
      </h4>
      <GitHubCalendar
        username="salimdotpy"
        blockSize={15}
        blockMargin={5}
        color={'#'+color}
        fontSize={16}
      />
    </div>
  );
}

export default Github;
