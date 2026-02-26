/* ═══════════════════════════════════════════════════════════════════
   Golf Studio - Invoice Scripts
   ═══════════════════════════════════════════════════════════════════ */

/**
 * Print the document
 */
function printDocument() {
    window.print();
}

/**
 * Show toast notification
 * @param {string} message 
 * @param {boolean} isError
 */
function showToast(message, isError = false) {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    
    if (isError) {
        toast.style.background = '#dc3545';
    } else {
        toast.style.background = '#0f5c3b';
    }
    
    toast.classList.add('show');
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 2500);
}

// Initialize on load
document.addEventListener('DOMContentLoaded', () => {
    console.log('Invoice initialized');
});
