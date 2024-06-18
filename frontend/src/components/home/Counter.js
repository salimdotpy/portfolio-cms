import React, { useState, useEffect, useRef } from 'react';

function Counter({ start, stop, duration }) {
    const [count, setCount] = useState(start);
    const { startTimer, stopTimer } = useSharedTimer(duration, setCount, stop);
    const counterRef = useRef(null);

    useEffect(() => {
        let currentCount = counterRef.current 
        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                startTimer();
            } else {
                stopTimer();
            }
        }, { threshold: 1.0 });

        observer.observe(currentCount);

        return () => {
            observer.unobserve(currentCount);
        };
    }, [startTimer, stopTimer, counterRef]);

    return (
        <span ref={counterRef}>
            {count}
        </span>
    );
}

const useSharedTimer = (duration, setCount, stop) => {
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
        }, duration * 100);
    };

    const stopTimer = () => {
        clearInterval(timerId.current);
    };

    useEffect(() => {
        return () => clearInterval(timerId.current);
    }, []);

    return { startTimer, stopTimer };
};

export default Counter;