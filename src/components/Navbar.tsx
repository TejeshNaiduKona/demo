import { User, Settings } from 'lucide-react'

export default function Navbar() {
  return (
    <header className="fixed inset-x-0 top-0 z-50 pointer-events-auto">
      <div className="flex items-center justify-between px-8 py-[18px]">
        <div className="flex items-center gap-3">
          <svg width="28" height="28" viewBox="0 0 28 28" fill="none" aria-hidden="true">
            <path d="M14 2L23.5 11.5L14 21L4.5 11.5L14 2Z" fill="#4ECDC4" opacity="1" />
            <path d="M15.9 5.5L25.4 15L15.9 24.5L6.4 15L15.9 5.5Z" fill="#4ECDC4" opacity="0.85" />
          </svg>
          <div className="font-heading text-[18px] font-semibold text-primaryText">Pallet Ross</div>
        </div>

        <nav className="flex items-center gap-1 overflow-x-auto whitespace-nowrap font-heading text-[14px] text-primaryText">
          <button className="cursor-pointer px-[14px] py-[8px]">Get Started</button>
          <button className="cursor-pointer flex items-center px-[14px] py-[8px]">
            <span className="mr-[6px] inline-block h-[14px] w-[14px] rounded-full bg-brandTeal" />
            Create strategy
          </button>
          <button className="cursor-pointer px-[14px] py-[8px]">Pricing</button>
          <button className="cursor-pointer px-[14px] py-[8px]">Contact</button>
          <button className="cursor-pointer px-[14px] py-[8px]">Solution</button>
          <button className="cursor-pointer px-[14px] py-[8px]">E-Commerce</button>
        </nav>

        <div className="flex items-center gap-2">
          <button className="rounded-md p-2 hover:bg-hoverBg" aria-label="User settings">
            <User size={20} strokeWidth={1.9} />
          </button>
          <button className="rounded-md p-2 hover:bg-hoverBg" aria-label="App settings">
            <Settings size={20} strokeWidth={1.9} />
          </button>
        </div>
      </div>
    </header>
  )
}
