import About from './About';
import Facts from './Facts';
import Services from './Services';
import Testimonials from './Testimonials';
import Skills from './Skills';
import Resume from './Resume';
import Contact from './Contact';
// import Portfolio from './components/Portfolio';
import Project from './Project';

function Home() {
  return (
    <>
    <About/>
    <Facts/>
    <Skills/>
    <Resume/>
    <Project/>
    <Services/>
    <Testimonials/>
    <Contact/>
  </>
  );
}
export default Home;