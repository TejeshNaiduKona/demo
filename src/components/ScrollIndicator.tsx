import { ChevronUp, ChevronDown } from 'lucide-react'

export default function ScrollIndicator() {
  const up = () => window.scrollBy({ top: -window.innerHeight, behavior: 'smooth' })
  const down = () => window.scrollBy({ top: window.innerHeight, behavior: 'smooth' })

  return (
    <div className="fixed right-6 top-1/2 z-40 flex -translate-y-1/2 flex-col gap-3">
      <button
        onClick={up}
        className="flex h-[36px] w-[36px] items-center justify-center rounded-lg border-[1.5px] border border-outlineBorder bg-transparent hover:bg-hoverBg"
        aria-label="Scroll up"
      >
        <ChevronUp size={16} strokeWidth={2} />
      </button>
      <button
        onClick={down}
        className="flex h-[36px] w-[36px] items-center justify-center rounded-lg border-[1.5px] border border-outlineBorder bg-transparent hover:bg-hoverBg"
        aria-label="Scroll down"
      >
        <ChevronDown size={16} strokeWidth={2} />
      </button>
    </div>
  )
}
