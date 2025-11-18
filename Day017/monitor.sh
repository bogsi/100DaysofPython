#!/bin/bash

while true; do
    clear
    echo "=================================="
    echo "        СИСТЕМЕН МОНИТОР"
    echo "=================================="
    echo
    
    # CPU информация
    echo "🖥️  CPU:"
    top -l 1 | grep "CPU usage" | awk '{print "   Използване: " $3 " (user) + " $5 " (sys)"}'
    
    # RAM информация  
    echo
    echo "💾 RAM:"
    vm_stat | awk '
    /Pages free/ { free = $3 * 4096 }
    /Pages active/ { active = $3 * 4096 }
    /Pages inactive/ { inactive = $3 * 4096 }
    /Pages wired/ { wired = $3 * 4096 }
    END {
        total = free + active + inactive + wired
        used = active + inactive + wired
        printf "   Общо: %.1f GB\n", total/1024/1024/1024
        printf "   Използвано: %.1f GB (%.1f%%)\n", used/1024/1024/1024, (used/total)*100
        printf "   Свободно: %.1f GB\n", free/1024/1024/1024
    }'
    
    # Дисково пространство
    echo
    echo "💿 Диск:"
    df -h / | tail -1 | awk '{print "   Използвано: " $3 " от " $2 " (" $5 ")"}'
    df -h / | tail -1 | awk '{print "   Свободно: " $4}'
    
    echo
    echo "⏰ $(date '+%H:%M:%S')"
    echo
    echo "Натисни Ctrl+C за изход"
    
    sleep 2
done