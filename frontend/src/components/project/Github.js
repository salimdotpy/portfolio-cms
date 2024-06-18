import React from "react";
import GitHubCalendar from "react-github-calendar";

function Github() {
  return (
    <div className="row justify-content-center py-3">
      <h4 className="project-heading pb-2">
        Days I <strong className="purple">Code</strong>
      </h4>
      <GitHubCalendar
        username="salimdotpy"
        blockSize={15}
        blockMargin={5}
        color="#c084f5"
        fontSize={16}
      />
    </div>
  );
}

export default Github;
