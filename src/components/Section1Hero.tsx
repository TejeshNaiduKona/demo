import { motion } from 'framer-motion'

const smoothEase = [0.22, 1, 0.36, 1] as const

function renderAnimatedWords(words: string[], delayStep: number, baseDelay = 0) {
  return words.map((word, wordIndex) => (
    <motion.span
      key={`${word}-${wordIndex}`}
      className="mr-[0.25em] inline-block"
      initial={{ opacity: 0, y: 28 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, ease: 'easeOut', delay: baseDelay + wordIndex * delayStep }}
    >
      {word}
    </motion.span>
  ))
}

export default function Section1Hero() {
  return (
    <section className="min-h-screen relative overflow-hidden" aria-label="Hero">
      <div className="mx-auto max-w-[1280px] px-8 pt-[140px] md:px-16">
        <h1 className="max-w-[1100px] font-heading text-[clamp(4.25rem,8vw,6rem)] font-extrabold leading-[1] tracking-[-0.06em] text-primaryText">
          <span className="block">{renderAnimatedWords(['A', 'place', 'to', 'display'], 0.08, 0)}</span>
          <span className="block">{renderAnimatedWords(['your', 'masterpiece.'], 0.08, 0.32)}</span>
        </h1>

        <div className="relative mt-10 h-[260px] w-full">
          <div className="absolute left-[calc(50%-320px)] top-[-12px] z-20">
            <motion.div
              className="relative inline-block rounded-full bg-brandBlue px-[18px] py-[8px] font-heading text-[15px] font-semibold text-white"
              initial={{ opacity: 0, scaleX: 1, scaleY: 1 }}
              animate={{ opacity: 1, scaleX: [1, 1.25, 0.75, 1.15, 0.95, 1.05, 1], scaleY: [1, 0.75, 1.25, 0.85, 1.05, 0.95, 1] }}
              transition={{ duration: 0.8, delay: 3.05, ease: 'easeOut' }}
            >
              @coplin
              <span
                aria-hidden
                className="absolute bottom-[-8px] left-[16px] h-0 w-0 border-l-[8px] border-r-[4px] border-t-[10px] border-l-transparent border-r-transparent border-t-brandBlue"
              />
            </motion.div>
          </div>

          <div className="absolute right-[calc(50%-420px)] top-[-20px] z-20">
            <motion.div
              className="relative inline-block rounded-full bg-brandGreen px-[18px] py-[8px] font-heading text-[15px] font-semibold text-white"
              initial={{ opacity: 0, scaleX: 1, scaleY: 1 }}
              animate={{ opacity: 1, scaleX: [1, 1.25, 0.75, 1.15, 0.95, 1.05, 1], scaleY: [1, 0.75, 1.25, 0.85, 1.05, 0.95, 1] }}
              transition={{ duration: 0.8, delay: 3.2, ease: 'easeOut' }}
            >
              @andrea
              <span
                aria-hidden
                className="absolute bottom-[-8px] right-[16px] h-0 w-0 border-l-[4px] border-r-[8px] border-t-[10px] border-l-transparent border-r-transparent border-t-brandGreen"
              />
            </motion.div>
          </div>
        </div>

        <motion.p
          className="mt-12 max-w-[480px] font-body text-[16px] leading-[1.6] text-bodyCopy"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 2.2, ease: 'easeOut' }}
        >
          Artists can display their masterpieces, and buyers can discover and purchase works that resonate with them.
        </motion.p>

        <motion.div
          className="mt-7 flex gap-4 pb-20"
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 2.4, ease: smoothEase }}
        >
          <button className="rounded-full bg-primaryText px-[28px] py-[14px] font-heading text-[15px] font-semibold text-white hover:bg-[#333333]">
            Join for $9.99/m
          </button>
          <button className="rounded-full px-[20px] py-[14px] font-heading text-[15px] font-medium text-primaryText hover:bg-[rgba(0,0,0,0.06)]">
            Read more
          </button>
        </motion.div>
      </div>
    </section>
  )
}
