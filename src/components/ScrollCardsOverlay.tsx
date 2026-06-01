import React, { useEffect, useMemo, useState } from 'react'
import { motion, useMotionValueEvent, useScroll, useTransform, type MotionValue } from 'framer-motion'

type Slot = { x: number; y: number; rotate: number; scale: number; z: number }
type Cascade = { top: number; left: number; rotate: number; z: number }
type LayoutState = {
  width: number
  height: number
  scrollableHeight: number
  lockProgress: number
  sectionTwoTop: number
  sectionTwoHeight: number
}

type OverlayProps = {
  containerRef: React.RefObject<HTMLDivElement | null>
}

const HERO_ROW_Y = 522
const smoothEase = [0.22, 1, 0.36, 1] as const
const hoverEase = [0.34, 1.56, 0.64, 1] as const
const introDelay = 0.8
const introDuration = 0.72
const travelToRightDuration = 0.6
const sweepLeftDuration = 1.6

const slots: Slot[] = [
  { x: -480, y: 18, rotate: -18, scale: 0.88, z: 1 },
  { x: -310, y: 6, rotate: -10, scale: 0.92, z: 2 },
  { x: -155, y: -2, rotate: -4, scale: 0.96, z: 3 },
  { x: 0, y: -8, rotate: 0, scale: 1, z: 4 },
  { x: 160, y: -2, rotate: 5, scale: 0.96, z: 3 },
  { x: 320, y: 6, rotate: 12, scale: 0.92, z: 2 },
  { x: 480, y: 18, rotate: 20, scale: 0.88, z: 1 },
]

const cascade: Cascade[] = Array.from({ length: 7 }, (_, index) => ({
  top: 300 + index * 70,
  left: 20 + index * 150,
  rotate: -3 + index * 3,
  z: 7 - index,
}))

function getTimeForProgress(progress: number, ease: readonly [number, number, number, number]) {
  const [, y1, , y2] = ease

  const bezierY = (t: number) => {
    const inverse = 1 - t
    return 3 * inverse * inverse * t * y1 + 3 * inverse * t * t * y2 + t * t * t
  }

  let low = 0
  let high = 1
  let mid = 0.5

  for (let iteration = 0; iteration < 24; iteration += 1) {
    mid = (low + high) / 2
    const value = bezierY(mid)
    if (value < progress) {
      low = mid
    } else {
      high = mid
    }
  }

  return mid
}

function artworkSrc(index: number) {
  return `/card-${index + 1}.png`
}

function ArtworkCardContent({ index }: { index: number }) {
  return (
    <div className="h-[220px] w-[220px] overflow-hidden rounded-[18px] bg-white shadow-[0_20px_60px_rgba(0,0,0,0.20)]">
      <img
        src={artworkSrc(index)}
        alt={`Artwork card ${index + 1}`}
        draggable={false}
        className="h-full w-full object-cover"
      />
    </div>
  )
}

function ArtworkCard({
  index,
  slot,
  cascadeItem,
  layout,
  scrollYProgress,
  introDone,
  revealDelay,
  revealDuration,
  onIntroComplete,
}: {
  index: number
  slot: Slot
  cascadeItem: Cascade
  layout: LayoutState
  scrollYProgress: MotionValue<number>
  introDone: boolean
  revealDelay: number
  revealDuration: number
  onIntroComplete?: () => void
}) {
  const [hovered, setHovered] = useState(false)
  const lp = Math.max(layout.lockProgress, 0.05)
  const p1 = lp * 0.33
  const p2 = lp * 0.66
  const clamped = useTransform(scrollYProgress, (value) => Math.min(value, lp))

  const s1Cx = layout.width / 2 + slot.x
  const s1Cy = HERO_ROW_Y + slot.y
  const stackCx = layout.width / 2
  const stackCy = layout.height / 2
  const cascadeLeftRef = layout.width * 0.4
  const s2Cx = cascadeLeftRef + cascadeItem.left + 110
  const s2Cy = cascadeItem.top + 110

  const x = useTransform(clamped, [0, p1, p2, lp], [s1Cx, stackCx, stackCx, s2Cx])
  const y = useTransform(clamped, [0, p1, p2, lp], [s1Cy, stackCy, s2Cy, s2Cy])
  const rotate = useTransform(clamped, [0, p1, lp], [slot.rotate, 0, cascadeItem.rotate])
  const scaleX = useTransform(clamped, [0, p1, lp], [slot.scale, 1, 1])
  const scaleY = useTransform(clamped, [0, p1, lp], [slot.scale, 1, 1])
  const zIndex = hovered ? 30 : cascadeItem.z

  if (introDone) {
    return (
      <motion.div
        className="pointer-events-auto"
        style={{
          position: 'absolute',
          left: 0,
          top: 0,
          x,
          y,
          rotate,
          scaleX,
          scaleY,
          zIndex,
          willChange: 'transform',
        }}
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
        whileHover={{ transition: { duration: 0.2, ease: hoverEase } }}
      >
        <ArtworkCardContent index={index} />
      </motion.div>
    )
  }

  const initialStyle = index === 0
    ? {
        opacity: 0,
        x: layout.width / 2,
        y: layout.height / 2 + 180,
        rotate: 0,
        scale: 0.3,
      }
    : {
        opacity: 0,
        x: s1Cx,
        y: s1Cy,
        rotate: slot.rotate,
        scale: slot.scale,
      }

  const animateStyle = index === 0
    ? {
        opacity: [0, 1, 1, 1],
        x: [layout.width / 2, layout.width / 2, layout.width / 2 + slots[6].x, layout.width / 2 + slots[0].x],
        y: [layout.height / 2 + 180, HERO_ROW_Y, HERO_ROW_Y + slots[6].y, HERO_ROW_Y + slots[0].y],
        rotate: [0, 0, slots[6].rotate, slots[0].rotate],
        scale: [0.3, 1, slots[6].scale, slots[0].scale],
      }
    : {
        opacity: 1,
        x: s1Cx,
        y: s1Cy,
        rotate: slot.rotate,
        scale: slot.scale,
      }

  const transition = index === 0
    ? ({
        delay: introDelay,
        duration: introDuration + travelToRightDuration + sweepLeftDuration,
        times: [0, introDuration / (introDuration + travelToRightDuration + sweepLeftDuration), (introDuration + travelToRightDuration) / (introDuration + travelToRightDuration + sweepLeftDuration), 1],
        ease: smoothEase,
      } as const)
    : ({
        delay: revealDelay,
        duration: revealDuration,
        ease: 'easeOut' as const,
      } as const)

  return (
    <motion.div
      className="pointer-events-auto"
      style={{
        position: 'absolute',
        left: 0,
        top: 0,
        zIndex,
        willChange: 'transform',
      }}
      initial={initialStyle}
      animate={animateStyle}
      transition={transition as any}
      onAnimationComplete={index === 0 ? onIntroComplete : undefined}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      whileHover={{ transition: { duration: 0.2, ease: hoverEase } }}
    >
      <ArtworkCardContent index={index} />
    </motion.div>
  )
}

export default function ScrollCardsOverlay({ containerRef }: OverlayProps) {
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ['start start', 'end end'],
  })

  const [layout, setLayout] = useState<LayoutState>(() => ({
    width: typeof window !== 'undefined' ? window.innerWidth : 1440,
    height: typeof window !== 'undefined' ? window.innerHeight : 900,
    scrollableHeight: typeof window !== 'undefined' ? Math.max(document.body.scrollHeight - window.innerHeight, 1) : 1,
    lockProgress: 0.72,
    sectionTwoTop: typeof window !== 'undefined' ? window.innerHeight : 0,
    sectionTwoHeight: typeof window !== 'undefined' ? window.innerHeight : 0,
  }))
  const [introDone, setIntroDone] = useState(false)
  const [currentProgress, setCurrentProgress] = useState(0)

  useMotionValueEvent(scrollYProgress, 'change', (value) => {
    setCurrentProgress(value)
  })

  useEffect(() => {
    setCurrentProgress(scrollYProgress.get())
  }, [scrollYProgress])

  useEffect(() => {
    let timeoutId: number | undefined

    const recompute = () => {
      const containerElement = containerRef.current
      const sectionTwoElement = containerElement?.querySelector<HTMLElement>('[data-section="two"]') ?? document.querySelector<HTMLElement>('[data-section="two"]')

      setLayout((current) => ({
        ...current,
        width: window.innerWidth,
        height: window.innerHeight,
      }))

      if (!sectionTwoElement) {
        return
      }

      const containerTop = (containerElement?.getBoundingClientRect().top ?? 0) + window.scrollY
      const scrollableHeight = Math.max(document.body.scrollHeight - window.innerHeight, 1)
      const sectionTwoRect = sectionTwoElement.getBoundingClientRect()
      const sectionTwoTop = sectionTwoRect.top + window.scrollY
      const sectionTwoHeight = sectionTwoRect.height
      const lockProgress = Math.min(Math.max((sectionTwoTop - containerTop) / scrollableHeight, 0.05), 0.99)

      setLayout((current) => ({
        ...current,
        scrollableHeight,
        lockProgress,
        sectionTwoTop,
        sectionTwoHeight,
      }))
    }

    const scheduleRecompute = () => {
      window.clearTimeout(timeoutId)
      timeoutId = window.setTimeout(recompute, 300)
    }

    recompute()
    window.addEventListener('resize', scheduleRecompute)

    return () => {
      if (timeoutId !== undefined) {
        window.clearTimeout(timeoutId)
      }
      window.removeEventListener('resize', scheduleRecompute)
    }
  }, [containerRef])

  const revealPlans = useMemo(() => {
    const sweepStart = introDelay + introDuration + travelToRightDuration

    return slots.map((_, index) => {
      if (index === 0) {
        return { delay: introDelay, duration: introDuration + travelToRightDuration + sweepLeftDuration }
      }

      const progress = (slots[index].x - slots[6].x) / (slots[0].x - slots[6].x)
      const revealTime = getTimeForProgress(progress, smoothEase)
      const revealDelay = sweepStart + revealTime * sweepLeftDuration
      const revealDuration = index <= 3 ? 0.06 : 0.18

      return { delay: revealDelay, duration: revealDuration }
    })
  }, [])

  const isLocked = currentProgress >= layout.lockProgress
  const wrapperStyle = isLocked
    ? { position: 'absolute' as const, top: layout.lockProgress * Math.max(layout.scrollableHeight, 1), left: 0, width: '100%', height: layout.height, zIndex: 5 }
    : { position: 'fixed' as const, inset: 0, zIndex: 5 }

  return (
    <div className="pointer-events-none" style={wrapperStyle}>
      <div className="relative h-full w-full">
        {slots.map((slot, index) => (
          <ArtworkCard
            key={`card-${index + 1}`}
            index={index}
            slot={slot}
            cascadeItem={cascade[index]}
            layout={layout}
            scrollYProgress={scrollYProgress}
            introDone={introDone}
            revealDelay={revealPlans[index].delay}
            revealDuration={revealPlans[index].duration}
            onIntroComplete={index === 0 ? () => setIntroDone(true) : undefined}
          />
        ))}
      </div>
    </div>
  )
}