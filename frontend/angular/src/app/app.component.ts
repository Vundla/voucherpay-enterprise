import { Component, OnInit } from '@angular/core';
import { AccessibilityService } from './services/accessibility.service';
import { AnalyticsService } from './services/analytics.service';
import { AuthService } from './services/auth.service';

@Component({
  selector: 'app-root',
  template: `
    <div class="app-container" 
         [attr.data-theme]="currentTheme"
         [class.high-contrast]="isHighContrast"
         [class.reduced-motion]="isReducedMotion">
      
      <!-- Skip Navigation Links -->
      <div class="skip-links" [attr.aria-label]="'Skip navigation links'">
        <a class="skip-link" href="#main-content" [attr.aria-label]="'Skip to main content'">
          Skip to main content
        </a>
        <a class="skip-link" href="#navigation" [attr.aria-label]="'Skip to navigation'">
          Skip to navigation
        </a>
        <a class="skip-link" href="#accessibility-menu" [attr.aria-label]="'Skip to accessibility menu'">
          Skip to accessibility menu
        </a>
      </div>

      <!-- Accessibility Toolbar -->
      <app-accessibility-toolbar 
        id="accessibility-menu"
        [attr.aria-label]="'Accessibility options'"
        (themeChange)="onThemeChange($event)"
        (fontSizeChange)="onFontSizeChange($event)"
        (contrastChange)="onContrastChange($event)"
        (motionChange)="onMotionChange($event)">
      </app-accessibility-toolbar>

      <!-- Main Navigation -->
      <nav id="navigation" 
           class="main-navigation" 
           role="navigation"
           [attr.aria-label]="'Main navigation'">
        <app-navigation 
          [user]="currentUser"
          [accessibilityPreferences]="accessibilityPreferences">
        </app-navigation>
      </nav>

      <!-- Main Content Area -->
      <main id="main-content" 
            class="main-content" 
            role="main"
            [attr.aria-label]="'Main content'">
        
        <!-- Live Region for Screen Reader Announcements -->
        <div id="live-region" 
             class="sr-only" 
             aria-live="polite" 
             aria-atomic="true"
             [attr.aria-label]="'Live announcements'">
          {{ liveRegionMessage }}
        </div>

        <!-- Page Title -->
        <h1 class="page-title sr-only" id="page-title">
          {{ pageTitle }}
        </h1>

        <!-- Empowerment Banner -->
        <section class="empowerment-banner" 
                 [attr.aria-labelledby]="'empowerment-title'"
                 *ngIf="showEmpowermentBanner">
          <h2 id="empowerment-title" class="empowerment-title">
            {{ empowermentMessage }}
          </h2>
          <p class="empowerment-description">
            Breaking barriers, creating opportunities, empowering lives.
          </p>
        </section>

        <!-- Router Outlet for Page Content -->
        <router-outlet></router-outlet>

        <!-- Loading Indicator -->
        <app-loading-spinner 
          *ngIf="isLoading"
          [attr.aria-label]="'Loading content'"
          [message]="loadingMessage">
        </app-loading-spinner>

        <!-- Toast Notifications -->
        <app-toast-container 
          [attr.aria-label]="'Notifications'"
          role="alert"
          aria-live="assertive">
        </app-toast-container>

      </main>

      <!-- Footer -->
      <footer class="main-footer" 
              role="contentinfo"
              [attr.aria-label]="'Footer information'">
        <app-footer 
          [accessibilityInfo]="accessibilityInfo"
          [empowermentResources]="empowermentResources">
        </app-footer>
      </footer>

    </div>
  `,
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'VoucherPay Enterprise - Inclusive Platform';
  
  // Accessibility state
  currentTheme = 'default';
  isHighContrast = false;
  isReducedMotion = false;
  accessibilityPreferences: any = {};
  
  // Application state
  currentUser: any = null;
  isLoading = false;
  loadingMessage = '';
  liveRegionMessage = '';
  pageTitle = 'Welcome to VoucherPay Enterprise';
  
  // Empowerment features
  showEmpowermentBanner = true;
  empowermentMessage = 'Welcome to Your Empowerment Platform';
  empowermentResources: any[] = [];
  accessibilityInfo: any = {};

  constructor(
    private accessibilityService: AccessibilityService,
    private analyticsService: AnalyticsService,
    private authService: AuthService
  ) {}

  ngOnInit() {
    this.initializeAccessibility();
    this.initializeAnalytics();
    this.loadUserPreferences();
    this.announcePageLoad();
  }

  private initializeAccessibility() {
    // Load accessibility preferences
    this.accessibilityService.getPreferences().subscribe(preferences => {
      this.accessibilityPreferences = preferences;
      this.applyAccessibilitySettings(preferences);
    });

    // Set up keyboard navigation
    this.setupKeyboardNavigation();
    
    // Initialize focus management
    this.setupFocusManagement();
  }

  private initializeAnalytics() {
    // Track empowerment engagement
    this.analyticsService.trackEmpowermentEngagement({
      feature: 'platform_access',
      timestamp: new Date(),
      accessibility_context: this.accessibilityPreferences
    });
  }

  private loadUserPreferences() {
    this.authService.getCurrentUser().subscribe(user => {
      this.currentUser = user;
      if (user?.accessibilityProfile) {
        this.applyAccessibilitySettings(user.accessibilityProfile);
      }
    });
  }

  private announcePageLoad() {
    setTimeout(() => {
      this.updateLiveRegion('VoucherPay Enterprise platform loaded. Use tab to navigate, or skip to main content.');
    }, 1000);
  }

  private setupKeyboardNavigation() {
    document.addEventListener('keydown', (event) => {
      // Escape key to close modals/menus
      if (event.key === 'Escape') {
        this.closeAllModals();
      }
      
      // Alt + 1 for main content
      if (event.altKey && event.key === '1') {
        event.preventDefault();
        this.focusElement('#main-content');
      }
      
      // Alt + 2 for navigation
      if (event.altKey && event.key === '2') {
        event.preventDefault();
        this.focusElement('#navigation');
      }
      
      // Alt + 3 for accessibility menu
      if (event.altKey && event.key === '3') {
        event.preventDefault();
        this.focusElement('#accessibility-menu');
      }
    });
  }

  private setupFocusManagement() {
    // Ensure focus is managed when content changes
    document.addEventListener('DOMContentLoaded', () => {
      this.manageFocus();
    });
  }

  onThemeChange(theme: string) {
    this.currentTheme = theme;
    this.accessibilityService.updateTheme(theme);
    this.updateLiveRegion(\`Theme changed to \${theme}\`);
  }

  onFontSizeChange(size: string) {
    this.accessibilityService.updateFontSize(size);
    this.updateLiveRegion(\`Font size changed to \${size}\`);
  }

  onContrastChange(enabled: boolean) {
    this.isHighContrast = enabled;
    this.accessibilityService.updateHighContrast(enabled);
    this.updateLiveRegion(\`High contrast \${enabled ? 'enabled' : 'disabled'}\`);
  }

  onMotionChange(reduced: boolean) {
    this.isReducedMotion = reduced;
    this.accessibilityService.updateReducedMotion(reduced);
    this.updateLiveRegion(\`Motion \${reduced ? 'reduced' : 'enabled'}\`);
  }

  private applyAccessibilitySettings(preferences: any) {
    if (preferences.highContrast) {
      this.isHighContrast = true;
    }
    if (preferences.reducedMotion) {
      this.isReducedMotion = true;
    }
    if (preferences.theme) {
      this.currentTheme = preferences.theme;
    }
  }

  private updateLiveRegion(message: string) {
    this.liveRegionMessage = message;
    // Clear after announcement
    setTimeout(() => {
      this.liveRegionMessage = '';
    }, 3000);
  }

  private focusElement(selector: string) {
    const element = document.querySelector(selector) as HTMLElement;
    if (element) {
      element.focus();
    }
  }

  private closeAllModals() {
    // Implementation to close any open modals or dropdowns
    document.querySelectorAll('[data-modal="true"]').forEach(modal => {
      (modal as any).close();
    });
  }

  private manageFocus() {
    // Ensure proper focus management for accessibility
    const focusableElements = document.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    
    if (focusableElements.length > 0) {
      (focusableElements[0] as HTMLElement).focus();
    }
  }
}