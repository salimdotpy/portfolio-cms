import React, { useState, useEffect, useRef } from 'react';

function ProgressBar ({ min, val }) {
    const [count, setCount] = useState(min);
    const { startTimer, stopTimer } = useSharedTimer(setCount, val);
    const progressRef = useRef(null);

    useEffect(() => {
        let currentProg = progressRef.current;
        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                startTimer();
            } else {
                stopTimer();
            }
        }, { threshold: 1.0 });

        observer.observe(currentProg);

        return () => {
            observer.unobserve(currentProg);
        };
    }, [startTimer, stopTimer, progressRef]);

    return (
        <div ref={progressRef} className="progress-bar" role="progressbar" aria-valuenow={val} aria-valuemin={min} aria-valuemax="100" style={{width: count+"%"}}></div>
    );
}

const useSharedTimer = (setCount, stop) => {
    const timerId = useRef(null);

    const startTimer = () => {
        timerId.current = setInterval(() => {
            setCount((prevCount) => {
                if (prevCount >= stop) {
                    clearInterval(timerId.current);
                    return prevCount;
                }
                return prevCount + 1;
            });
        }, 10);
    };

    const stopTimer = () => {
        clearInterval(timerId.current);
    };

    useEffect(() => {
        return () => clearInterval(timerId.current);
    }, []);

    return { startTimer, stopTimer };
};

export default ProgressBar;