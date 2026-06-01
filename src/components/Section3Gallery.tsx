import { useEffect, useState } from 'react'
import { motion } from 'framer-motion'
import { ChevronLeft, ChevronRight } from 'lucide-react'

function renderAnimatedWords(words: string[], delayStep: number, baseDelay = 0) {
  return words.map((word, wordIndex) => (
    <motion.span
      key={`${word}-${wordIndex}`}
      className="mr-[0.2em] inline-block"
      initial={{ opacity: 0, filter: 'blur(10px)', y: 20 }}
      whileInView={{ opacity: 1, filter: 'blur(0px)', y: 0 }}
      viewport={{ once: true }}
      transition={{ duration: 0.5, ease: 'easeOut', delay: baseDelay + wordIndex * delayStep }}
    >
      {word}
    </motion.span>
  ))
}

export default function Section3Gallery(){
  const [active, setActive] = useState(0)
  useEffect(()=>{
    const id = setInterval(()=> setActive(s => (s+1)%3), 3000)
    return ()=> clearInterval(id)
  },[])

  return (
    <section data-section="three" className="relative min-h-screen overflow-hidden bg-pageBg px-8 py-20 md:px-16">
      <div className="max-w-6xl">
        <div className="relative z-10 mb-10 max-w-[520px]">
          <motion.div
            className="mb-5 font-heading text-[11px] font-medium tracking-[0.18em] text-eyebrow"
            initial={{ opacity: 0, filter: 'blur(8px)', y: 12 }}
            whileInView={{ opacity: 1, filter: 'blur(0px)', y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.55, ease: 'easeOut' }}
          >
            CLASS BY REATHA C. PHELAN
          </motion.div>
          <h2 className="font-heading text-[clamp(4rem,7vw,5rem)] font-extrabold leading-[1] tracking-[-0.075em] text-primaryText">
            {renderAnimatedWords(['Gateway', 'to', 'artist', 'people.'], 0.07, 0)}
          </h2>
        </div>

        <motion.div
          className="relative h-[600px] w-full overflow-hidden rounded-[24px] bg-primaryText"
          initial={{ opacity: 0, y: 40, filter: 'blur(12px)' }}
          whileInView={{ opacity: 1, y: 0, filter: 'blur(0px)' }}
          viewport={{ once: true, margin: '-60px' }}
          transition={{ duration: 0.8, ease: 'easeOut', delay: 0.4 }}
        >
          {['/banner-1.png', '/banner-2.png', '/banner-3.png'].map((src, index) => (
            <motion.img
              key={src}
              src={src}
              alt="Artwork banner"
              draggable={false}
              className="absolute inset-0 h-full w-full object-cover object-top"
              initial={false}
              animate={{ opacity: active === index ? 1 : 0, scale: active === index ? 1 : 1.04 }}
              transition={{ duration: 0.5, ease: 'easeInOut' }}
            />
          ))}

          <div className="absolute right-6 top-6 z-10 flex gap-[5px]">
            {[0, 1, 2].map((index) => (
              <button
                key={index}
                type="button"
                onClick={() => setActive(index)}
                className="h-[6px] rounded-full transition-all duration-300 ease-in-out"
                style={{
                  width: active === index ? 18 : 6,
                  backgroundColor: active === index ? 'rgba(255,255,255,0.95)' : 'rgba(255,255,255,0.45)',
                }}
                aria-label={`Go to slide ${index + 1}`}
              />
            ))}
          </div>

          <div className="absolute bottom-7 left-7 z-10 inline-block">
            <span
              aria-hidden
              className="pointer-events-none absolute inset-[-8px] rounded-full border-2 border-white/40"
              style={{ animation: 'pulse-ring-1 2s ease-out infinite' }}
            />
            <span
              aria-hidden
              className="pointer-events-none absolute inset-[-4px] rounded-full border-2 border-white/25"
              style={{ animation: 'pulse-ring-2 2s ease-out infinite' }}
            />
            <motion.button
              type="button"
              className="relative z-20 inline-flex items-center gap-2 rounded-full bg-white px-[28px] py-[12px] font-heading text-[15px] font-semibold text-primaryText"
              whileHover={{ scale: 1.05 }}
              transition={{ duration: 0.2 }}
            >
              Watch
            </motion.button>
          </div>

          <div className="absolute bottom-7 right-7 z-10 flex gap-2.5">
            <motion.button
              type="button"
              onClick={() => setActive((current) => (current - 1 + 3) % 3)}
              aria-label="Previous slide"
              className="flex h-[44px] w-[44px] items-center justify-center rounded-full bg-white/90 text-primaryText shadow-[0_4px_16px_rgba(0,0,0,0.15)]"
              whileHover={{ scale: 1.08, backgroundColor: '#FFFFFF' }}
              transition={{ duration: 0.2 }}
            >
              <ChevronLeft size={20} strokeWidth={2} />
            </motion.button>
            <motion.button
              type="button"
              onClick={() => setActive((current) => (current + 1) % 3)}
              aria-label="Next slide"
              className="flex h-[44px] w-[44px] items-center justify-center rounded-full bg-white/90 text-primaryText shadow-[0_4px_16px_rgba(0,0,0,0.15)]"
              whileHover={{ scale: 1.08, backgroundColor: '#FFFFFF' }}
              transition={{ duration: 0.2 }}
            >
              <ChevronRight size={20} strokeWidth={2} />
            </motion.button>
          </div>
        </motion.div>
      </div>
    </section>
  )
}
