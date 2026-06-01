import { useRef } from 'react'
import { motion, useInView } from 'framer-motion'

function renderAnimatedWords(words: string[], delayStep: number, baseDelay = 0) {
  return words.map((word, wordIndex) => (
    <motion.span
      key={`${word}-${wordIndex}`}
      className="mr-[0.25em] inline-block"
      initial={{ opacity: 0, filter: 'blur(10px)', y: 20 }}
      whileInView={{ opacity: 1, filter: 'blur(0px)', y: 0 }}
      viewport={{ once: true, margin: '-80px' }}
      transition={{ duration: 0.5, ease: 'easeOut', delay: baseDelay + wordIndex * delayStep }}
    >
      {word}
    </motion.span>
  ))
}

export default function Section2Showcase(){
  const sectionRef = useRef<HTMLElement | null>(null)
  const tagsInView = useInView(sectionRef, { amount: 0.95, once: true })

  return (
    <section ref={sectionRef} data-section="two" className="relative min-h-[calc(100vh-30px)] overflow-hidden bg-pageBg px-8 py-20 md:px-16">
      <div className="flex max-w-6xl items-start gap-12">
        <div className="w-full max-w-[520px] pt-8">
          <motion.div
            className="mb-5 font-heading text-[11px] font-medium tracking-[0.18em] text-eyebrow"
            initial={{ opacity: 0, filter: 'blur(8px)', y: 16 }}
            whileInView={{ opacity: 1, filter: 'blur(0px)', y: 0 }}
            viewport={{ once: true, margin: '-80px' }}
            transition={{ duration: 0.6, ease: 'easeOut' }}
          >
            E-COMMERCE
          </motion.div>

          <h2 className="font-heading text-[clamp(3rem,5.5vw,3.75rem)] font-extrabold leading-[1.05] tracking-[-0.06em] text-primaryText">
            <span className="block">{renderAnimatedWords(['Showcase,', 'Sell'], 0.06, 0)}</span>
            <span className="block text-brandRed">{renderAnimatedWords(['&', 'acquire', 'arts', 'to'], 0.06, 0.24)}</span>
            <span className="block">{renderAnimatedWords(['our', 'marketplace.'], 0.06, 0.48)}</span>
          </h2>

          <motion.p
            className="mt-7 max-w-[340px] font-body text-[15px] leading-[1.65] text-bodyCopy"
            initial={{ opacity: 0, filter: 'blur(8px)', y: 16 }}
            whileInView={{ opacity: 1, filter: 'blur(0px)', y: 0 }}
            viewport={{ once: true, margin: '-80px' }}
            transition={{ duration: 0.6, delay: 0.5, ease: 'easeOut' }}
          >
            Dynamic community where artists and buyers seamlessly merge. ArtFusion brings together creators and enthusiasts to share creativity.
          </motion.p>

          <motion.div
            className="mt-12 flex gap-3"
            initial={{ opacity: 0, y: 16 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: '-80px' }}
            transition={{ duration: 0.5, delay: 0.7, ease: 'easeOut' }}
          >
            <button className="rounded-full bg-primaryText px-[28px] py-[14px] font-heading text-[15px] font-semibold text-white hover:bg-[#333333]">
              Join for $9.99/m
            </button>
            <button className="rounded-full border-[1.5px] border border-outlineBorder px-[20px] py-[14px] font-heading text-[15px] font-medium text-primaryText hover:bg-hoverBg">
              Read more
            </button>
          </motion.div>

          <motion.div
            className="pointer-events-none fixed left-[calc(40%+340px)] top-[260px] z-20"
            initial={{ opacity: 0, scale: 0.6 }}
            animate={tagsInView ? { opacity: 1, scale: 1 } : { opacity: 0, scale: 0.6 }}
            transition={{ duration: 0.5, ease: 'easeOut' }}
          >
            <div className="relative inline-block rounded-full bg-brandRed px-[20px] py-[9px] font-heading text-[15px] font-semibold text-white">
              @howard
              <span
                aria-hidden
                className="absolute bottom-[-9px] left-1/2 h-0 w-0 -translate-x-1/2 border-l-[8px] border-r-[8px] border-t-[10px] border-l-transparent border-r-transparent border-t-brandRed"
              />
            </div>
          </motion.div>

          <motion.div
            className="pointer-events-none fixed left-[calc(40%+680px)] top-[430px] z-20"
            initial={{ opacity: 0, scale: 0.6 }}
            animate={tagsInView ? { opacity: 1, scale: 1 } : { opacity: 0, scale: 0.6 }}
            transition={{ duration: 0.5, delay: 0.15, ease: 'easeOut' }}
          >
            <div className="relative inline-block rounded-full bg-primaryText px-[20px] py-[9px] font-heading text-[15px] font-semibold text-white">
              @robin
              <span
                aria-hidden
                className="absolute bottom-[-9px] left-[20px] h-0 w-0 border-l-[8px] border-r-[8px] border-t-[10px] border-l-transparent border-r-transparent border-t-primaryText"
              />
            </div>
          </motion.div>
        </div>

        <div className="relative min-h-[520px] flex-1">
          {/* Right side intentionally empty — cards will cascade here */}
        </div>
      </div>
    </section>
  )
}
