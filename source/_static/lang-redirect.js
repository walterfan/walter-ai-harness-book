/* lang-redirect.js
 *
 * Loaded only by book/build/html/index.html (the root chooser page).
 * Inspects `navigator.language` once and redirects to the matching
 * per-language subtree. Falls back silently — the chooser page also
 * renders two visible links so users whose browsers block the redirect
 * (or who arrive with scripts disabled) still reach a language version.
 */

(function () {
    'use strict';

    var SUPPORTED = { en: 'en/', 'zh-cn': 'zh_CN/', 'zh-sg': 'zh_CN/' };

    function pickLanguage() {
        var candidates = [];
        if (navigator.languages && navigator.languages.length) {
            candidates = navigator.languages.slice();
        } else if (navigator.language) {
            candidates.push(navigator.language);
        }
        for (var i = 0; i < candidates.length; i++) {
            var tag = candidates[i].toLowerCase();
            if (SUPPORTED[tag]) return SUPPORTED[tag];
            // Accept bare primary tag ("zh" → zh_CN) for convenience.
            var primary = tag.split('-')[0];
            if (primary === 'zh') return SUPPORTED['zh-cn'];
            if (primary === 'en') return SUPPORTED.en;
        }
        return SUPPORTED.en; // default — English is the source language
    }

    try {
        var target = pickLanguage();
        // Use replace() so the chooser page does not leave a history entry.
        window.location.replace('./' + target);
    } catch (e) {
        // Leave the user on the chooser page; the visible fallback links
        // will carry them the rest of the way.
    }
})();
