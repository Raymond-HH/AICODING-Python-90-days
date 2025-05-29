/**
 * Python 90天学习系统 - 主要JavaScript文件
 * 提供交互功能和用户体验增强
 */

// 全局变量
window.PythonLearningSystem = {
    version: '2.0.0',
    initialized: false
};

// DOM加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
    initializeSystem();
});

/**
 * 系统初始化
 */
function initializeSystem() {
    console.log('🐍 Python学习系统初始化中...');
    
    // 初始化提示框
    initializeTooltips();
    
    // 初始化进度动画
    initializeProgressAnimations();
    
    // 初始化导航高亮
    initializeNavigation();
    
    // 初始化响应式特性
    initializeResponsive();
    
    // 标记为已初始化
    window.PythonLearningSystem.initialized = true;
    console.log('✅ Python学习系统初始化完成');
}

/**
 * 初始化提示框
 */
function initializeTooltips() {
    // 如果Bootstrap的tooltip可用，则启用
    if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
}

/**
 * 初始化进度条动画
 */
function initializeProgressAnimations() {
    const progressBars = document.querySelectorAll('.progress-bar');
    
    // 延迟启动动画以获得更好的视觉效果
    setTimeout(function() {
        progressBars.forEach(function(bar) {
            const targetWidth = bar.style.width || bar.getAttribute('data-width');
            if (targetWidth) {
                bar.style.width = '0%';
                bar.style.transition = 'width 1.5s ease-in-out';
                
                // 稍后设置目标宽度
                setTimeout(function() {
                    bar.style.width = targetWidth;
                }, 100);
            }
        });
    }, 300);
}

/**
 * 初始化导航高亮
 */
function initializeNavigation() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(function(link) {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
}

/**
 * 初始化响应式特性
 */
function initializeResponsive() {
    // 监听窗口大小变化
    window.addEventListener('resize', function() {
        handleWindowResize();
    });
    
    // 初始检查
    handleWindowResize();
}

/**
 * 处理窗口大小变化
 */
function handleWindowResize() {
    const width = window.innerWidth;
    
    // 在小屏幕上自动收起导航栏
    if (width < 768) {
        const navbarCollapse = document.querySelector('.navbar-collapse');
        if (navbarCollapse && navbarCollapse.classList.contains('show')) {
            const navbarToggler = document.querySelector('.navbar-toggler');
            if (navbarToggler) {
                navbarToggler.click();
            }
        }
    }
}

/**
 * 显示成功消息
 */
function showSuccessMessage(message, duration = 3000) {
    showNotification(message, 'success', duration);
}

/**
 * 显示错误消息
 */
function showErrorMessage(message, duration = 5000) {
    showNotification(message, 'danger', duration);
}

/**
 * 显示信息消息
 */
function showInfoMessage(message, duration = 3000) {
    showNotification(message, 'info', duration);
}

/**
 * 显示通知
 */
function showNotification(message, type = 'info', duration = 3000) {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px; max-width: 500px;';
    
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    document.body.appendChild(notification);
    
    // 自动移除
    if (duration > 0) {
        setTimeout(function() {
            if (notification.parentNode) {
                notification.remove();
            }
        }, duration);
    }
}

/**
 * 复制文本到剪贴板
 */
function copyToClipboard(text) {
    return navigator.clipboard.writeText(text).then(function() {
        showSuccessMessage('已复制到剪贴板');
        return true;
    }).catch(function(err) {
        console.error('复制失败:', err);
        showErrorMessage('复制失败，请手动复制');
        return false;
    });
}

/**
 * 格式化日期
 */
function formatDate(date) {
    if (typeof date === 'string') {
        date = new Date(date);
    }
    
    const now = new Date();
    const diff = now - date;
    const seconds = Math.floor(diff / 1000);
    const minutes = Math.floor(seconds / 60);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);
    
    if (days > 0) {
        return days === 1 ? '1天前' : `${days}天前`;
    } else if (hours > 0) {
        return hours === 1 ? '1小时前' : `${hours}小时前`;
    } else if (minutes > 0) {
        return minutes === 1 ? '1分钟前' : `${minutes}分钟前`;
    } else {
        return '刚刚';
    }
}

/**
 * 防抖函数
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = function() {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * 节流函数
 */
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(function() {
                inThrottle = false;
            }, limit);
        }
    };
}

/**
 * 滚动到顶部
 */
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

/**
 * 检查元素是否在视口中
 */
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

/**
 * 添加淡入动画
 */
function addFadeInAnimation(elements) {
    if (typeof elements === 'string') {
        elements = document.querySelectorAll(elements);
    } else if (elements.length === undefined) {
        elements = [elements];
    }
    
    elements.forEach(function(element, index) {
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        element.style.transition = 'all 0.6s ease-out';
        
        setTimeout(function() {
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }, index * 100);
    });
}

/**
 * 验证表单
 */
function validateForm(form) {
    const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
    let isValid = true;
    
    inputs.forEach(function(input) {
        if (!input.value.trim()) {
            input.classList.add('is-invalid');
            isValid = false;
        } else {
            input.classList.remove('is-invalid');
            input.classList.add('is-valid');
        }
    });
    
    return isValid;
}

/**
 * 加载状态管理
 */
const LoadingManager = {
    show: function(element, text = '加载中...') {
        if (typeof element === 'string') {
            element = document.querySelector(element);
        }
        
        if (element) {
            const spinner = document.createElement('div');
            spinner.className = 'loading-overlay d-flex align-items-center justify-content-center';
            spinner.style.cssText = `
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(255, 255, 255, 0.8);
                z-index: 1000;
            `;
            
            spinner.innerHTML = `
                <div class="text-center">
                    <div class="spinner-border text-primary" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                    <div class="mt-2 small text-muted">${text}</div>
                </div>
            `;
            
            element.style.position = 'relative';
            element.appendChild(spinner);
        }
    },
    
    hide: function(element) {
        if (typeof element === 'string') {
            element = document.querySelector(element);
        }
        
        if (element) {
            const overlay = element.querySelector('.loading-overlay');
            if (overlay) {
                overlay.remove();
            }
        }
    }
};

// 导出到全局
window.PythonLearningSystem = Object.assign(window.PythonLearningSystem, {
    showSuccessMessage,
    showErrorMessage,
    showInfoMessage,
    showNotification,
    copyToClipboard,
    formatDate,
    debounce,
    throttle,
    scrollToTop,
    isInViewport,
    addFadeInAnimation,
    validateForm,
    LoadingManager
}); 