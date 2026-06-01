import { useRef } from 'react'
import Navbar from './components/Navbar'
import DecorativeBlobs from './components/DecorativeBlobs'
import ScrollIndicator from './components/ScrollIndicator'
import ScrollCardsOverlay from './components/ScrollCardsOverlay'
import Section1Hero from './components/Section1Hero'
import Section2Showcase from './components/Section2Showcase'
import Section3Gallery from './components/Section3Gallery'

function App() {
  const containerRef = useRef<HTMLDivElement | null>(null)

  return (
    <div ref={containerRef} className="relative isolate min-h-screen overflow-x-hidden bg-pageBg text-primaryText font-sans">
      <DecorativeBlobs />
      <Navbar />
      <ScrollIndicator />

      <ScrollCardsOverlay containerRef={containerRef} />

      <main className="relative z-0">
        <Section1Hero />
        <Section2Showcase />
        <Section3Gallery />
      </main>
    </div>
  )
}

export default App
